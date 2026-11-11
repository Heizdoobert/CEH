import sys
sys.path.insert(0, "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets")
from dk_b17_L1080_python import LRUPageReplacer

# Test with 3 physical frames
lru = LRUPageReplacer(physical_frames=3)

# 1. Fill 3 frames with read misses: VPN 1, 2, 3
pfn1, fault1 = lru.access(vpn=1, is_write=False)
pfn2, fault2 = lru.access(vpn=2, is_write=False)
pfn3, fault3 = lru.access(vpn=3, is_write=True) # Page 3 is dirty!

assert fault1 and fault2 and fault3
assert lru.total_page_faults == 3
assert lru.total_disk_writes == 0
assert list(lru.frames.keys()) == [1, 2, 3]

# 2. Access VPN 1 (Hit): moves 1 to end -> order is [2, 3, 1]
pfn1_again, fault_hit = lru.access(vpn=1, is_write=False)
assert not fault_hit
assert pfn1_again == pfn1
assert list(lru.frames.keys()) == [2, 3, 1]

# 3. Access VPN 4 (Miss): should evict VPN 2 (clean)
# Allocated PFN should reuse VPN 2's frame (PFN 1)
pfn4, fault4 = lru.access(vpn=4, is_write=False)
assert fault4
assert lru.total_page_faults == 4
assert lru.total_disk_writes == 0 # VPN 2 was clean, no disk write!
assert list(lru.frames.keys()) == [3, 1, 4]

# 4. Access VPN 5 (Miss): should evict VPN 3 (DIRTY!)
# Evicting dirty page 3 MUST increment total_disk_writes!
pfn5, fault5 = lru.access(vpn=5, is_write=False)
assert fault5
assert lru.total_page_faults == 5
assert lru.total_disk_writes == 1 # Dirty write-back triggered!
assert list(lru.frames.keys()) == [1, 4, 5]

print("LRUPageReplacer Results:")
print(f"  Total page faults: {lru.total_page_faults}")
print(f"  Total disk writes (writebacks): {lru.total_disk_writes}")
print(f"  Current resident pages: {list(lru.frames.keys())}")

assert lru.total_page_faults == 5
assert lru.total_disk_writes == 1
assert list(lru.frames.keys()) == [1, 4, 5]
print("LRUPageReplacer verified successfully: LRU order, hit updates, page fault tracking, and dirty writeback confirmed!")
