import heapq

# Linux CFS weights from sched_prio_to_weight
NICE_0_LOAD = 1024
WEIGHT_NICE_0 = 1024
WEIGHT_NICE_5 = 335

class CFSTask:
    def __init__(self, pid: int, nice: int, weight: int):
        self.pid = pid
        self.nice = nice
        self.weight = weight
        self.vruntime = 0.0
        self.runtime_accum = 0.0

    def __lt__(self, other):
        return self.vruntime < other.vruntime

def simulate_cfs(total_wall_ticks=10000, tick_slice=1.0):
    t_a = CFSTask(pid=1, nice=0, weight=1024)
    t_b = CFSTask(pid=2, nice=5, weight=335)

    pq = [t_a, t_b]
    heapq.heapify(pq)

    for _ in range(total_wall_ticks):
        # Pick task with min vruntime (O(1) cached leftmost in Linux RB-tree)
        current = heapq.heappop(pq)
        
        # Run for tick_slice
        current.runtime_accum += tick_slice
        delta_vruntime = tick_slice * (NICE_0_LOAD / current.weight)
        current.vruntime += delta_vruntime

        heapq.heappush(pq, current)

    ratio_actual = t_a.runtime_accum / t_b.runtime_accum
    ratio_expected = 1024 / 335
    print(f"CFS Simulation Results over {total_wall_ticks} ticks:")
    print(f"  Task A (nice 0, weight 1024): runtime={t_a.runtime_accum:.1f}, vruntime={t_a.vruntime:.1f}")
    print(f"  Task B (nice 5, weight 335):  runtime={t_b.runtime_accum:.1f}, vruntime={t_b.vruntime:.1f}")
    print(f"  CPU Share Ratio (A / B): {ratio_actual:.4f} (Expected: {ratio_expected:.4f})")
    print(f"  Relative difference: {abs(ratio_actual - ratio_expected) / ratio_expected * 100:.3f}%")

    assert abs(ratio_actual - ratio_expected) / ratio_expected < 0.01, "CFS CPU share ratio deviated > 1%!"
    print("CFS Scheduler simulation verified successfully: Perfectly converges to ideal multi-tasking weights!")

if __name__ == "__main__":
    simulate_cfs()
