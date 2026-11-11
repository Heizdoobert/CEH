import numpy as np
from typing import List, Tuple, Optional

class BankersAlgorithm:
    def __init__(self, allocation: List[List[int]], max_claim: List[List[int]], available: List[int]):
        self.allocation = np.array(allocation, dtype=int)
        self.max_claim = np.array(max_claim, dtype=int)
        self.available = np.array(available, dtype=int)
        self.n_processes, self.n_resources = self.allocation.shape
        self.need = self.max_claim - self.allocation

    def is_safe(self, available: np.ndarray, allocation: np.ndarray, need: np.ndarray) -> Tuple[bool, List[int]]:
        work = available.copy()
        finish = [False] * self.n_processes
        safe_sequence = []

        while len(safe_sequence) < self.n_processes:
            found = False
            for p in range(self.n_processes):
                if not finish[p] and np.all(need[p] <= work):
                    work += allocation[p]
                    finish[p] = True
                    safe_sequence.append(p)
                    found = True
                    break
            if not found:
                break

        is_safe_state = len(safe_sequence) == self.n_processes
        return is_safe_state, safe_sequence

    def request_resources(self, pid: int, request: List[int]) -> Tuple[bool, str, Optional[List[int]]]:
        req = np.array(request, dtype=int)

        # Condition 1: Request <= Need
        if not np.all(req <= self.need[pid]):
            return False, f"Error: Process P{pid} exceeded its maximum claim! Need={self.need[pid]}, Req={req}", None

        # Condition 2: Request <= Available
        if not np.all(req <= self.available):
            return False, f"Process P{pid} must wait: insufficient available resources! Avail={self.available}, Req={req}", None

        # Speculative allocation
        avail_prime = self.available - req
        alloc_prime = self.allocation.copy()
        alloc_prime[pid] += req
        need_prime = self.need.copy()
        need_prime[pid] -= req

        safe, seq = self.is_safe(avail_prime, alloc_prime, need_prime)
        if safe:
            return True, f"Request granted! Speculative state is Safe with sequence: {[f'P{i}' for i in seq]}", seq
        else:
            return False, "Request DENIED: Speculative allocation results in an UNSAFE state!", None

def test_banker():
    alloc = [
        [0, 1, 0], # P0
        [2, 0, 0], # P1
        [3, 0, 2], # P2
        [2, 1, 1], # P3
        [0, 0, 2]  # P4
    ]
    max_c = [
        [7, 5, 3], # P0
        [3, 2, 2], # P1
        [9, 0, 2], # P2
        [2, 2, 2], # P3
        [4, 3, 3]  # P4
    ]
    avail = [3, 3, 2]

    banker = BankersAlgorithm(alloc, max_c, avail)

    print("=== Step 1: Need Matrix ===")
    expected_need = [
        [7, 4, 3],
        [1, 2, 2],
        [6, 0, 0],
        [0, 1, 1],
        [4, 3, 1]
    ]
    for i in range(5):
        print(f"  P{i}: Need={banker.need[i].tolist()} (Expected: {expected_need[i]})")
        assert np.array_equal(banker.need[i], expected_need[i]), f"Mismatch in Need for P{i}!"

    print("\n=== Step 2: Safety Check at T0 ===")
    safe, seq = banker.is_safe(banker.available, banker.allocation, banker.need)
    print(f"  System Safe: {safe}, Safe Sequence: {[f'P{i}' for i in seq]}")
    assert safe is True
    assert seq == [1, 3, 0, 2, 4] or seq == [1, 3, 4, 0, 2]

    print("\n=== Step 3: Test Request1 = (1, 0, 2) from P1 ===")
    granted, msg, seq1 = banker.request_resources(pid=1, request=[1, 0, 2])
    print(f"  Granted: {granted}")
    print(f"  Message: {msg}")
    assert granted is True
    assert seq1 is not None

    print("\n=== Step 4: Test Adversarial Unsafe Request from P4: (3, 3, 0) ===")
    granted4, msg4, _ = banker.request_resources(pid=4, request=[3, 3, 0])
    print(f"  Granted: {granted4}")
    print(f"  Message: {msg4}")
    assert granted4 is False, "Unsafe request should have been rejected!"

    print("\n=== Step 5: Test Exceeding Max Claim from P0: (0, 5, 0) ===")
    granted0, msg0, _ = banker.request_resources(pid=0, request=[0, 5, 0]) # Need[0] is (7, 4, 3), requesting 5 B exceeds need!
    print(f"  Granted: {granted0}")
    print(f"  Message: {msg0}")
    assert granted0 is False

    print("\nBanker's Algorithm verified successfully: All mathematical steps in Section 6.4 & Problem 3.6 empirically verified!")

if __name__ == "__main__":
    test_banker()
