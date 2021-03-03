import json

import click

from .runner import REGISTRY
from .util import Connection, register_benchmarks


register_benchmarks()
BENCHMARKS = {}
for benchmark in REGISTRY:
    BENCHMARKS[benchmark.name] = benchmark


if not BENCHMARKS:
    click.echo(click.style("\nNo benchmarks registered.", fg="red"))
    tip_msg = "(run conbench from a directory containing benchmarks).\n"
    click.echo(click.style(tip_msg, fg="yellow"))


@click.group()
def conbench():
    """Conbench: Language-independent Continuous Benchmarking (CB) Framework"""
    pass


@conbench.command(name="compare")
@click.argument("baseline")
@click.argument("contender")
@click.option(
    "--kind",
    default="batch",
    show_default=True,
    type=click.Choice(["batch", "benchmark", "run"], case_sensitive=False),
)
@click.option(
    "--threshold",
    default=5,
    show_default=True,
    type=int,
    help="(percent)",
)
def compare(baseline, contender, kind, threshold):
    """Compare benchmark runs."""

    connection = Connection()
    if kind == "batch":
        result = connection.compare_batches(baseline, contender, threshold)
    elif kind == "benchmark":
        result = connection.compare_benchmarks(baseline, contender, threshold)
    elif kind == "run":
        result = connection.compare_runs(baseline, contender, threshold)
    print(json.dumps(result, indent=2))


def _option(params, name, default, _type, help_msg=None):
    params.append(
        click.Option(
            (name,),
            type=_type,
            default=default,
            help=help_msg,
            show_default=True,
        )
    )


def _choice(params, name, choices):
    params.append(
        click.Option(
            (name,),
            default=choices[0],
            show_default=False,
            type=click.Choice(choices, case_sensitive=False),
        )
    )


def _help(benchmark, name, cases, tags):
    if not cases:
        description = getattr(benchmark, "description", f"Run {name} benchmark.")
        return description

    valid = [list(zip(tags, case)) for case in cases]
    benchmarks = [[f"{option}={value}" for option, value in case] for case in valid]
    examples = "\b\n".join([" ".join(example) for example in benchmarks])
    description = getattr(benchmark, "description", f"Run {name} benchmark(s).")
    examples = f"\b\nValid benchmark combinations:\n{examples}"
    note = "For each benchmark option, the first option value is the default."
    all_cases = f"\b\nTo run all combinations:\n$ conbench {name} --all=true"
    return f"{description}\n\n{note}\n\n{examples}\n\n{all_cases}"


def _to_cli_name(name):
    return f"--{name.replace('_', '-')}"


for name, benchmark in BENCHMARKS.items():
    params = []

    instance = benchmark()
    fields, cases = instance.fields, instance.cases
    options = benchmark.options if hasattr(benchmark, "options") else {}
    arguments = benchmark.arguments if hasattr(benchmark, "arguments") else []
    tags = [_to_cli_name(tag) for tag in fields]
    external = getattr(benchmark, "external", False)

    for k, v in instance.case_options.items():
        _choice(params, _to_cli_name(k), sorted(v))

    for argument in arguments:
        params.append(click.Argument((argument,)))
    if cases:
        _option(params, "--all", "false", bool)
    for option, config in options.items():
        if "choices" in config:
            _choice(params, _to_cli_name(option), config["choices"])
        else:
            help_msg = config.get("help", None)
            _option(
                params,
                _to_cli_name(option),
                config.get("default"),
                config["type"],
                help_msg=help_msg,
            )
    if not external:
        _option(params, "--iterations", 1, int)
        _option(params, "--gc-collect", "true", bool)
        _option(params, "--gc-disable", "true", bool)
    _option(params, "--show-result", "true", bool)
    _option(params, "--show-output", "false", bool)

    params.append(
        click.Option(
            ("--run-id",),
            type=str,
            help="Group executions together with a run id.",
        )
    )

    def _benchmark(
        show_result,
        show_output,
        benchmark=benchmark,
        **kwargs,
    ):
        for result, output in benchmark().run(**kwargs):
            if show_output:
                click.echo()
                click.echo(click.style("Benchmark output:", fg="yellow"))
                click.echo(click.style(str(output), fg="blue"))
            if show_result:
                click.echo()
                click.echo(click.style("Benchmark result:", fg="yellow"))
                json_result = json.dumps(result, indent=4, sort_keys=True)
                click.echo(click.style(json_result, fg="green"))
            del output

    conbench.add_command(
        click.Command(
            name,
            params=params,
            callback=_benchmark,
            help=_help(benchmark, name, cases, tags),
        )
    )
