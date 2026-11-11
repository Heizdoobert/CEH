#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b16_L986_c.c"

int main(void) {
    printf("Testing dk_b16: x86-64 4-Level Page Table Translation & PTE Bitfield...\n");

    /* 1. Verify PTE union size equals 8 bytes (64 bits) */
    assert(sizeof(x86_64_pte_t) == 8);

    /* 2. Verify bitfield packing */
    x86_64_pte_t pte;
    pte.raw = 0;
    pte.bits.present = 1;
    pte.bits.rw = 1;
    pte.bits.user_supervisor = 1;
    pte.bits.no_execute = 1;
    pte.bits.pfn = 0x123456789AULL;

    assert(pte.bits.present == 1);
    assert(pte.bits.rw == 1);
    assert(pte.bits.user_supervisor == 1);
    assert(pte.bits.no_execute == 1);
    assert(pte.bits.pfn == 0x123456789AULL);
    assert((pte.raw & 0x1) == 1); /* Present is bit 0 */
    assert((pte.raw >> 63) == 1); /* NX is bit 63 */

    /* 3. Verify Virtual Address Decomposition */
    uint64_t vaddr = 0x00007A3B5C7D9E00ULL;
    page_walk_indices_t idx = decompose_virtual_address(vaddr);

    /* Reconstruct 48-bit address */
    uint64_t reconstructed = ((uint64_t)idx.pml4_idx << 39) |
                             ((uint64_t)idx.pdpt_idx << 30) |
                             ((uint64_t)idx.pd_idx   << 21) |
                             ((uint64_t)idx.pt_idx   << 12) |
                             ((uint64_t)idx.offset);

    assert(reconstructed == (vaddr & 0x0000FFFFFFFFFFFFULL));

    printf("dk_b16 verified successfully: PTE size = %zu bytes, PML4=%u, PDPT=%u, PD=%u, PT=%u, Offset=0x%X\n",
           sizeof(x86_64_pte_t), idx.pml4_idx, idx.pdpt_idx, idx.pd_idx, idx.pt_idx, idx.offset);
    return 0;
}
