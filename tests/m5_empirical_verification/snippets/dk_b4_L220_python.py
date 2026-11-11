import threading
import queue
import time
from typing import List

class ThreadWorkerPool:
    # Production thread pool pattern demonstrating queue-based work distribution
    def __init__(self, num_workers: int):
        self.work_queue: queue.Queue = queue.Queue()
        self.results: List[int] = []
        self.lock: threading.Lock = threading.Lock()
        self.workers: List[threading.Thread] = []
        self.shutdown_sentinel = object()

        for worker_id in range(num_workers):
            t = threading.Thread(target=self._worker_loop, args=(worker_id,))
            t.daemon = True
            t.start()
            self.workers.append(t)

    def _worker_loop(self, worker_id: int) -> None:
        while True:
            item = self.work_queue.get()
            if item is self.shutdown_sentinel:
                self.work_queue.task_done()
                break
            
            # Simulated CPU-bound or I/O work
            result = item * item

            with self.lock:
                self.results.append(result)
            
            self.work_queue.task_done()

    def submit(self, value: int) -> None:
        self.work_queue.put(value)

    def wait_completion(self) -> None:
        self.work_queue.join()
        for _ in self.workers:
            self.work_queue.put(self.shutdown_sentinel)
        for t in self.workers:
            t.join()

if __name__ == "__main__":
    pool = ThreadWorkerPool(num_workers=4)
    for num in range(10):
        pool.submit(num)
    pool.wait_completion()
    print(f"Processed results count: {len(pool.results)}")
