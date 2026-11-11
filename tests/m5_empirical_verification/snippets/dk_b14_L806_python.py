from collections import deque
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class MLFQTask:
    pid: int
    total_cpu_needed: int
    cpu_executed: int = 0
    priority_level: int = 0
    time_spent_in_level: int = 0

class MLFQScheduler:
    def __init__(self, num_levels=3, quantums=(10, 20, 40), boost_interval=200):
        self.num_levels = num_levels
        self.quantums = quantums
        self.boost_interval = boost_interval
        self.queues: List[deque] = [deque() for _ in range(num_levels)]
        self.current_time = 0

    def add_task(self, task: MLFQTask):
        task.priority_level = 0
        task.time_spent_in_level = 0
        self.queues[0].append(task)

    def step(self) -> Optional[int]:
        self.current_time += 1

        # Periodic Priority Boost (Rule 5: Anti-starvation)
        if self.current_time % self.boost_interval == 0:
            for lvl in range(1, self.num_levels):
                while self.queues[lvl]:
                    t = self.queues[lvl].popleft()
                    t.priority_level = 0
                    t.time_spent_in_level = 0
                    self.queues[0].append(t)

        # Select highest priority non-empty queue (Rule 1)
        active_task = None
        for lvl in range(self.num_levels):
            if self.queues[lvl]:
                active_task = self.queues[lvl][0]
                break

        if not active_task:
            return None # Idle CPU

        # Execute 1 tick
        active_task.cpu_executed += 1
        active_task.time_spent_in_level += 1

        # Task completion check
        if active_task.cpu_executed >= active_task.total_cpu_needed:
            self.queues[active_task.priority_level].popleft()
            return active_task.pid

        # Quantum expiration check (Rule 4: Demotion)
        current_lvl = active_task.priority_level
        if active_task.time_spent_in_level >= self.quantums[current_lvl]:
            self.queues[current_lvl].popleft()
            active_task.time_spent_in_level = 0
            if current_lvl < self.num_levels - 1:
                active_task.priority_level += 1
            self.queues[active_task.priority_level].append(active_task)

        return active_task.pid
