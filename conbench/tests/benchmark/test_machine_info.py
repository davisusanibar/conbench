from ...machine_info import (
    _fill_from_cpuinfo,
    _fill_from_lscpu,
    _fill_from_meminfo,
    _round_memory,
)

L1D_CACHE = 524288
L1I_CACHE = 524288
L2_CACHE = 16777216
L3_CACHE = 23068672
MEMORY = 131590280000
FREQUENCY = 4500000000


LSCPU = [
    "Architecture:                    x86_64",
    "CPU op-mode(s):                  32-bit, 64-bit",
    "Byte Order:                      Little Endian",
    "Address sizes:                   46 bits physical, 48 bits virtual",
    "CPU(s):                          32",
    "On-line CPU(s) list:             0-31",
    "Thread(s) per core:              2",
    "Core(s) per socket:              16",
    "Socket(s):                       1",
    "NUMA node(s):                    1",
    "Vendor ID:                       GenuineIntel",
    "CPU family:                      6",
    "Model:                           85",
    "Model name:                      Intel(R) Core(TM) i9-9960X CPU @ 3.10GHz",
    "Stepping:                        4",
    "CPU MHz:                         1577.989",
    "CPU max MHz:                     4500.0000",
    "CPU min MHz:                     1200.0000",
    "BogoMIPS:                        6199.99",
    "Virtualization:                  VT-x",
    "L1d cache:                       524288",
    "L1i cache:                       524288",
    "L2 cache:                        16777216",
    "L3 cache:                        23068672",
    "NUMA node0 CPU(s):               0-31",
    "Vulnerability Itlb multihit:     KVM: Mitigation: VMX disabled",
    "Vulnerability L1tf:              Mitigation; PTE Inversion; VMX conditional cache flushes, SMT vulnerable",
    "Vulnerability Mds:               Mitigation; Clear CPU buffers; SMT vulnerable",
    "Vulnerability Meltdown:          Mitigation; PTI",
    "Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp",
    "Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization",
    "Vulnerability Spectre v2:        Mitigation; Full generic retpoline, IBPB conditional, IBRS_FW, STIBP conditional, RSB filling",
    "Vulnerability Srbds:             Not affected",
    "Vulnerability Tsx async abort:   Mitigation; Clear CPU buffers; SMT vulnerable",
    "Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cdp_l3 invpcid_single pti ssbd mba ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm mpx rdt_a avx512f avx512dq rdseed adx smap clflushopt clwb intel_pt avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req md_clear flush_l1d",
]


MEMINFO = [
    "MemTotal:       131590280 kB",
    "MemFree:        112655968 kB",
    "MemAvailable:   129464936 kB",
    "Buffers:          603140 kB",
    "Cached:         16374620 kB",
    "SwapCached:            0 kB",
    "Active:         15203728 kB",
    "Inactive:        2326196 kB",
    "Active(anon):     312872 kB",
    "Inactive(anon):     2352 kB",
    "Active(file):   14890856 kB",
    "Inactive(file):  2323844 kB",
    "Unevictable:           0 kB",
    "Mlocked:               0 kB",
    "SwapTotal:       2097148 kB",
    "SwapFree:        2097148 kB",
    "Dirty:                 8 kB",
    "Writeback:             0 kB",
    "AnonPages:        552160 kB",
    "Mapped:           221996 kB",
    "Shmem:              4156 kB",
    "KReclaimable:     848396 kB",
    "Slab:            1187156 kB",
    "SReclaimable:     848396 kB",
    "SUnreclaim:       338760 kB",
    "KernelStack:       12112 kB",
    "PageTables:         9780 kB",
    "NFS_Unstable:          0 kB",
    "Bounce:                0 kB",
    "WritebackTmp:          0 kB",
    "CommitLimit:    67892288 kB",
    "Committed_AS:    3204896 kB",
    "VmallocTotal:   34359738367 kB",
    "VmallocUsed:       66336 kB",
    "VmallocChunk:          0 kB",
    "Percpu:            25344 kB",
    "HardwareCorrupted:     0 kB",
    "AnonHugePages:    172032 kB",
    "ShmemHugePages:        0 kB",
    "ShmemPmdMapped:        0 kB",
    "FileHugePages:         0 kB",
    "FilePmdMapped:         0 kB",
    "HugePages_Total:       0",
    "HugePages_Free:        0",
    "HugePages_Rsvd:        0",
    "HugePages_Surp:        0",
    "Hugepagesize:       2048 kB",
    "Hugetlb:               0 kB",
    "DirectMap4k:      566608 kB",
    "DirectMap2M:    26359808 kB",
    "DirectMap1G:    106954752 kB",
]


CPUINFO = {
    "python_version": "3.8.5.final.0 (64 bit)",
    "cpuinfo_version": [7, 0, 0],
    "cpuinfo_version_string": "7.0.0",
    "arch": "X86_64",
    "bits": 64,
    "count": 32,
    "arch_string_raw": "x86_64",
    "vendor_id_raw": "GenuineIntel",
    "brand_raw": "Intel(R) Core(TM) i9-9960X CPU @ 3.10GHz",
    "hz_advertised_friendly": "3.1000 GHz",
    "hz_actual_friendly": "1.7795 GHz",
    "hz_advertised": [3100000000, 0],
    "hz_actual": [1779488000, 0],
    "stepping": 4,
    "model": 85,
    "family": 6,
    "flags": [
        "3dnowprefetch",
        "abm",
        "acpi",
        "adx",
        "aes",
        "aperfmperf",
        "apic",
        "arat",
        "arch_perfmon",
        "art",
        "avx",
        "avx2",
        "avx512bw",
        "avx512cd",
        "avx512dq",
        "avx512f",
        "avx512vl",
        "bmi1",
        "bmi2",
        "bts",
        "cat_l3",
        "cdp_l3",
        "clflush",
        "clflushopt",
        "clwb",
        "cmov",
        "constant_tsc",
        "cpuid",
        "cpuid_fault",
        "cqm",
        "cqm_llc",
        "cqm_mbm_local",
        "cqm_mbm_total",
        "cqm_occup_llc",
        "cx16",
        "cx8",
        "dca",
        "de",
        "ds_cpl",
        "dtes64",
        "dtherm",
        "dts",
        "epb",
        "ept",
        "ept_ad",
        "erms",
        "est",
        "f16c",
        "flexpriority",
        "flush_l1d",
        "fma",
        "fpu",
        "fsgsbase",
        "fxsr",
        "hle",
        "ht",
        "hwp",
        "hwp_act_window",
        "hwp_epp",
        "hwp_pkg_req",
        "ibpb",
        "ibrs",
        "ida",
        "intel_pt",
        "invpcid",
        "invpcid_single",
        "lahf_lm",
        "lm",
        "mba",
        "mca",
        "mce",
        "md_clear",
        "mmx",
        "monitor",
        "movbe",
        "mpx",
        "msr",
        "mtrr",
        "nonstop_tsc",
        "nopl",
        "nx",
        "osxsave",
        "pae",
        "pat",
        "pbe",
        "pcid",
        "pclmulqdq",
        "pdcm",
        "pdpe1gb",
        "pebs",
        "pge",
        "pln",
        "pni",
        "popcnt",
        "pqe",
        "pqm",
        "pse",
        "pse36",
        "pti",
        "pts",
        "rdrand",
        "rdrnd",
        "rdseed",
        "rdt_a",
        "rdtscp",
        "rep_good",
        "rtm",
        "sdbg",
        "sep",
        "smap",
        "smep",
        "ss",
        "ssbd",
        "sse",
        "sse2",
        "sse4_1",
        "sse4_2",
        "ssse3",
        "stibp",
        "syscall",
        "tm",
        "tm2",
        "tpr_shadow",
        "tsc",
        "tsc_adjust",
        "tsc_deadline_timer",
        "tscdeadline",
        "vme",
        "vmx",
        "vnmi",
        "vpid",
        "x2apic",
        "xgetbv1",
        "xsave",
        "xsavec",
        "xsaveopt",
        "xsaves",
        "xtopology",
        "xtpr",
    ],
    "l3_cache_size": 23068672,
    "l2_cache_size": "16 MiB",
    "l1_data_cache_size": "512 KiB",
    "l1_instruction_cache_size": "512 KiB",
    "l2_cache_line_size": 256,
    "l2_cache_associativity": 6,
}


def test_machine_info_from_lscpu():
    info = {
        "cpu_l1d_cache_bytes": "",
        "cpu_l1i_cache_bytes": "",
        "cpu_l2_cache_bytes": "",
        "cpu_l3_cache_bytes": "",
        "cpu_frequency_max_hz": "",
    }
    _fill_from_lscpu(info, LSCPU)
    assert info == {
        "cpu_l1d_cache_bytes": L1D_CACHE,
        "cpu_l1i_cache_bytes": L1I_CACHE,
        "cpu_l2_cache_bytes": L2_CACHE,
        "cpu_l3_cache_bytes": L3_CACHE,
        "cpu_frequency_max_hz": FREQUENCY,
    }


def test_machine_info_from_meminfo():
    info = {"memory_bytes": ""}
    _fill_from_meminfo(info, MEMINFO)
    assert info == {"memory_bytes": MEMORY}


def test_machine_info_from_cpuinfo():
    info = {
        "cpu_model_name": "",
        "cpu_l1d_cache_bytes": "",
        "cpu_l1i_cache_bytes": "",
        "cpu_l2_cache_bytes": "",
        "cpu_l3_cache_bytes": "",
    }
    _fill_from_cpuinfo(info, CPUINFO)
    assert info == {
        "cpu_model_name": "Intel(R) Core(TM) i9-9960X CPU @ 3.10GHz",
        "cpu_l1d_cache_bytes": L1D_CACHE,
        "cpu_l1i_cache_bytes": L1I_CACHE,
        "cpu_l2_cache_bytes": L2_CACHE,
        "cpu_l3_cache_bytes": L3_CACHE,
    }


def test_fill_order():
    info = {
        "memory_bytes": "",
        "cpu_model_name": "",
        "cpu_l1d_cache_bytes": "",
        "cpu_l1i_cache_bytes": "",
        "cpu_l2_cache_bytes": "",
        "cpu_l3_cache_bytes": "",
        "cpu_frequency_max_hz": "",
    }
    _fill_from_meminfo(info, MEMINFO)
    _fill_from_lscpu(info, LSCPU)
    _fill_from_cpuinfo(info, CPUINFO)
    assert info == {
        "memory_bytes": MEMORY,
        "cpu_model_name": "Intel(R) Core(TM) i9-9960X CPU @ 3.10GHz",
        "cpu_l1d_cache_bytes": L1D_CACHE,
        "cpu_l1i_cache_bytes": L1I_CACHE,
        "cpu_l2_cache_bytes": L2_CACHE,
        "cpu_l3_cache_bytes": L3_CACHE,
        "cpu_frequency_max_hz": FREQUENCY,
    }


def test_round_memory():
    before = [131590280000, 131593068000, 131593872000]
    after = [132070244352, 132070244352, 132070244352]
    assert list(map(_round_memory, before)) == after

    before = [15855024000, 15855036000, 15855040000]
    after = [16106127360, 16106127360, 16106127360]
    assert list(map(_round_memory, before)) == after
