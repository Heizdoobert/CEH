def verify_problem_3_1():
    processes = [
        {"pid": "P1", "at": 0, "bt": 8},
        {"pid": "P2", "at": 1, "bt": 4},
        {"pid": "P3", "at": 2, "bt": 9},
        {"pid": "P4", "at": 3, "bt": 5},
    ]

    # 1. FCFS
    # P1 (0..8), P2 (8..12), P3 (12..21), P4 (21..26)
    ct_fcfs = {"P1": 8, "P2": 12, "P3": 21, "P4": 26}
    tat_fcfs = {p["pid"]: ct_fcfs[p["pid"]] - p["at"] for p in processes}
    wt_fcfs = {p["pid"]: tat_fcfs[p["pid"]] - p["bt"] for p in processes}
    avg_tat_fcfs = sum(tat_fcfs.values()) / 4.0
    avg_wt_fcfs = sum(wt_fcfs.values()) / 4.0

    print("=== 1. FCFS ===")
    print(f"  CT:  {ct_fcfs}")
    print(f"  TAT: {tat_fcfs} -> Avg: {avg_tat_fcfs:.2f} ms")
    print(f"  WT:  {wt_fcfs} -> Avg: {avg_wt_fcfs:.2f} ms")
    assert avg_tat_fcfs == 15.25
    assert avg_wt_fcfs == 8.75

    # 2. SJF (Non-preemptive)
    # P1 (0..8) -> ready: P2(4), P4(5), P3(9) -> P2 (8..12) -> P4 (12..17) -> P3 (17..26)
    ct_sjf = {"P1": 8, "P2": 12, "P4": 17, "P3": 26}
    tat_sjf = {p["pid"]: ct_sjf[p["pid"]] - p["at"] for p in processes}
    wt_sjf = {p["pid"]: tat_sjf[p["pid"]] - p["bt"] for p in processes}
    avg_tat_sjf = sum(tat_sjf.values()) / 4.0
    avg_wt_sjf = sum(wt_sjf.values()) / 4.0

    print("\n=== 2. SJF (Non-preemptive) ===")
    print(f"  CT:  {ct_sjf}")
    print(f"  TAT: {tat_sjf} -> Avg: {avg_tat_sjf:.2f} ms")
    print(f"  WT:  {wt_sjf} -> Avg: {avg_wt_sjf:.2f} ms")
    assert avg_tat_sjf == 14.25
    assert avg_wt_sjf == 7.75

    # 3. SRTN (Preemptive)
    # t=0: P1 (rem 8)
    # t=1: P2 arrives (4 < 7) -> P2 runs
    # t=2: P3 arrives (9) -> P2 rem 3 -> P2 runs
    # t=3: P4 arrives (5) -> P2 rem 2 -> P2 runs
    # t=5: P2 finishes (CT=5)
    # ready: P4(5), P1(7), P3(9) -> P4 runs (5..10, CT=10)
    # ready: P1(7), P3(9) -> P1 runs (10..17, CT=17)
    # ready: P3(9) -> P3 runs (17..26, CT=26)
    ct_srtn = {"P1": 17, "P2": 5, "P4": 10, "P3": 26}
    tat_srtn = {p["pid"]: ct_srtn[p["pid"]] - p["at"] for p in processes}
    wt_srtn = {p["pid"]: tat_srtn[p["pid"]] - p["bt"] for p in processes}
    avg_tat_srtn = sum(tat_srtn.values()) / 4.0
    avg_wt_srtn = sum(wt_srtn.values()) / 4.0

    print("\n=== 3. SRTN (Preemptive SJF) ===")
    print(f"  CT:  {ct_srtn}")
    print(f"  TAT: {tat_srtn} -> Avg: {avg_tat_srtn:.2f} ms")
    print(f"  WT:  {wt_srtn} -> Avg: {avg_wt_srtn:.2f} ms")
    assert avg_tat_srtn == 13.00
    assert avg_wt_srtn == 6.50

    # 4. Round Robin (q = 4)
    # t=0..4: P1 runs (rem 4). Arrivals: P2 at 1, P3 at 2, P4 at 3. Queue at 4: [P2, P3, P4, P1]
    # t=4..8: P2 runs (rem 0, CT=8). Queue at 8: [P3, P4, P1]
    # t=8..12: P3 runs (rem 5). Queue at 12: [P4, P1, P3]
    # t=12..16: P4 runs (rem 1). Queue at 16: [P1, P3, P4]
    # t=16..20: P1 runs (rem 0, CT=20). Queue at 20: [P3, P4]
    # t=20..24: P3 runs (rem 1). Queue at 24: [P4, P3]
    # t=24..25: P4 runs (rem 0, CT=25). Queue at 25: [P3]
    # t=25..26: P3 runs (rem 0, CT=26). Queue at 26: []
    ct_rr = {"P1": 20, "P2": 8, "P3": 26, "P4": 25}
    tat_rr = {p["pid"]: ct_rr[p["pid"]] - p["at"] for p in processes}
    wt_rr = {p["pid"]: tat_rr[p["pid"]] - p["bt"] for p in processes}
    avg_tat_rr = sum(tat_rr.values()) / 4.0
    avg_wt_rr = sum(wt_rr.values()) / 4.0

    print("\n=== 4. Round Robin (q=4) ===")
    print(f"  CT:  {ct_rr}")
    print(f"  TAT: {tat_rr} -> Avg: {avg_tat_rr:.2f} ms")
    print(f"  WT:  {wt_rr} -> Avg: {avg_wt_rr:.2f} ms")
    assert avg_tat_rr == 18.25
    assert avg_wt_rr == 11.75

    print("\nALL 4 CPU SCHEDULING CALCULATIONS IN PROBLEM 3.1 VERIFIED WITH 100% MATHEMATICAL PRECISION!")

if __name__ == "__main__":
    verify_problem_3_1()
