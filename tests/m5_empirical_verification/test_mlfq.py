import sys
sys.path.insert(0, "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets")
from dk_b14_L806_python import MLFQScheduler, MLFQTask

scheduler = MLFQScheduler(num_levels=3, quantums=(10, 20, 40), boost_interval=200)

# Long-running task needing 500 CPU ticks
task1 = MLFQTask(pid=1, total_cpu_needed=500)
scheduler.add_task(task1)
assert task1.priority_level == 0

# Run 10 ticks: task1 should demote to level 1
for _ in range(10):
    scheduler.step()
print(f"Tick 10: task1.level={task1.priority_level}")
assert task1.priority_level == 1

# Short interactive task
task2 = MLFQTask(pid=2, total_cpu_needed=5)
scheduler.add_task(task2)

# Next 5 ticks: task2 preempts task1
for _ in range(5):
    pid = scheduler.step()
    assert pid == 2

print(f"Task 2 completed at tick {scheduler.current_time}")
assert task2.cpu_executed == 5

# Run 20 ticks of task1 at level 1: demotes to level 2
for _ in range(20):
    pid = scheduler.step()
    assert pid == 1

print(f"Tick {scheduler.current_time}: task1.level={task1.priority_level}")
assert task1.priority_level == 2

# Advance until tick 199: task1 is running in level 2
while scheduler.current_time < 199:
    scheduler.step()

print(f"Tick {scheduler.current_time}: task1.level={task1.priority_level}")
assert task1.priority_level == 2

# Step tick 200: priority boost MUST boost task1 to level 0!
scheduler.step()
print(f"Tick {scheduler.current_time} (after boost): task1.level={task1.priority_level}")
assert task1.priority_level == 0, "Task 1 should be boosted to level 0 at boost_interval=200!"

print("MLFQScheduler verified successfully: All 5 rules empirically confirmed!")
