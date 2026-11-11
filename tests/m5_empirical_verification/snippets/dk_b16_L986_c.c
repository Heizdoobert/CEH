#include <stdint.h>
#include <stdio.h>

typedef union {
    struct {
        uint64_t present        : 1;   /* Bit 0: 1 = in physical memory, 0 = Page Fault */
        uint64_t rw             : 1;   /* Bit 1: 0 = Read-only, 1 = Read/Write */
        uint64_t user_supervisor: 1;   /* Bit 2: 0 = Kernel mode only, 1 = User space accessible */
        uint64_t pwt            : 1;   /* Bit 3: Page-level write-through */
        uint64_t pcd            : 1;   /* Bit 4: Page-level cache disable */
        uint64_t accessed       : 1;   /* Bit 5: 1 = CPU has read/written this page */
        uint64_t dirty          : 1;   /* Bit 6: 1 = CPU has written to this page */
        uint64_t pat            : 1;   /* Bit 7: Page Attribute Table index */
        uint64_t global         : 1;   /* Bit 8: Global translation (not flushed on CR3 reload) */
        uint64_t ignored1       : 3;   /* Bits 9-11: Available for OS software use */
        uint64_t pfn            : 40;  /* Bits 12-51: Physical Frame Number (PFN) */
        uint64_t ignored2       : 11;  /* Bits 52-62: Available for OS software use */
        uint64_t no_execute     : 1;   /* Bit 63: XD/NX bit: 1 = Instruction fetch prohibited */
    } bits;
    uint64_t raw;
} x86_64_pte_t;

/* C simulation of x86-64 4-level virtual address decomposition */
typedef struct {
    uint16_t pml4_idx;
    uint16_t pdpt_idx;
    uint16_t pd_idx;
    uint16_t pt_idx;
    uint16_t offset;
} page_walk_indices_t;

page_walk_indices_t decompose_virtual_address(uint64_t vaddr) {
    page_walk_indices_t indices;
    indices.pml4_idx = (vaddr >> 39) & 0x1FF; /* Mask 9 bits (0..511) */
    indices.pdpt_idx = (vaddr >> 30) & 0x1FF;
    indices.pd_idx   = (vaddr >> 21) & 0x1FF;
    indices.pt_idx   = (vaddr >> 12) & 0x1FF;
    indices.offset   = vaddr & 0xFFF;         /* Mask 12 bits (0..4095) */
    return indices;
}
