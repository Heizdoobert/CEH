import threading
import time

class DiningPhilosophersMonitor:
    # Python solution for Dining Philosophers using threading.Condition
    def __init__(self, num_philosophers=5):
        self.num = num_philosophers
        self.state = ['THINKING'] * self.num
        self.cv = threading.Condition()

    def _left(self, i): return (i + self.num - 1) % self.num
    def _right(self, i): return (i + 1) % self.num

    def take_forks(self, i: int) -> None:
        with self.cv:
            self.state[i] = 'HUNGRY'
            while self.state[self._left(i)] == 'EATING' or self.state[self._right(i)] == 'EATING':
                self.cv.wait()
            self.state[i] = 'EATING'

    def put_forks(self, i: int) -> None:
        with self.cv:
            self.state[i] = 'THINKING'
            self.cv.notify_all()
