from collections import OrderedDict
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class PageMetadata:
    pfn: int
    vpn: int
    dirty: bool = False

class LRUPageReplacer:
    # Production simulation of LRU Page Frame Allocator with Dirty Write-Back tracking
    def __init__(self, physical_frames: int):
        self.capacity = physical_frames
        self.frames: OrderedDict[int, PageMetadata] = OrderedDict() # VPN -> PageMetadata
        self.next_free_pfn = 0
        self.total_page_faults = 0
        self.total_disk_writes = 0

    def access(self, vpn: int, is_write: bool = False) -> Tuple[int, bool]:
        # Returns (pfn, was_page_fault)
        if vpn in self.frames:
            # TLB / Cache Hit: Mark most recently used
            meta = self.frames[vpn]
            if is_write:
                meta.dirty = True
            self.frames.move_to_end(vpn)
            return meta.pfn, False

        # Page Fault Condition
        self.total_page_faults += 1

        if len(self.frames) >= self.capacity:
            # Evict Least Recently Used page (first item in OrderedDict)
            evicted_vpn, evicted_meta = self.frames.popitem(last=False)
            if evicted_meta.dirty:
                self.total_disk_writes += 1 # Write-back dirty page to swap/disk
            allocated_pfn = evicted_meta.pfn
        else:
            allocated_pfn = self.next_free_pfn
            self.next_free_pfn += 1

        new_meta = PageMetadata(pfn=allocated_pfn, vpn=vpn, dirty=is_write)
        self.frames[vpn] = new_meta
        return allocated_pfn, True
