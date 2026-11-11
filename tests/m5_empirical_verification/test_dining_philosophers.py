import sys
import os
import threading
import time

sys.path.insert(0, "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets")
from dk_b9_L604_python import DiningPhilosophersMonitor

monitor = DiningPhilosophersMonitor(num_philosophers=5)
meals_eaten = [0] * 5
MEALS_TARGET = 30
errors = []

def philosopher_worker(phil_id: int):
    for _ in range(MEALS_TARGET):
        # Think
        time.sleep(0.001)

        # Acquire forks
        monitor.take_forks(phil_id)

        # In critical section (eating): check neighbor state
        with monitor.cv:
            left = monitor._left(phil_id)
            right = monitor._right(phil_id)
            if monitor.state[left] == 'EATING' or monitor.state[right] == 'EATING':
                errors.append(f"VIOLATION: Phil {phil_id} eating while neighbor ({left} or {right}) also eating!")
            meals_eaten[phil_id] += 1

        time.sleep(0.002)

        # Release forks
        monitor.put_forks(phil_id)

threads = [threading.Thread(target=philosopher_worker, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print("Dining Philosophers Results:")
for i in range(5):
    print(f"  Philosopher {i} ate {meals_eaten[i]} meals")

assert len(errors) == 0, f"Encountered errors: {errors}"
assert all(m == MEALS_TARGET for m in meals_eaten), "Not all philosophers ate target meals!"
print("DiningPhilosophersMonitor verified successfully: 0 violations, all meals completed without deadlock!")
