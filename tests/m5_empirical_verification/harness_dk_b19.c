#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b19_L1203_c.c"

int main(void) {
    printf("Testing dk_b19: Ext4 Extent Tree Headers & Structures...\n");

    /* Standard ext4 extent structures are exactly 12 bytes each */
    printf("sizeof(struct ext4_extent_header) = %zu bytes\n", sizeof(struct ext4_extent_header));
    printf("sizeof(struct ext4_extent) = %zu bytes\n", sizeof(struct ext4_extent));

    assert(sizeof(struct ext4_extent_header) == 12);
    assert(sizeof(struct ext4_extent) == 12);

    struct ext4_extent_header hdr = {
        .eh_magic = 0xF30A,
        .eh_entries = 1,
        .eh_max = 4,
        .eh_depth = 0,
        .eh_generation = 1
    };

    assert(hdr.eh_magic == 0xF30A);
    assert(hdr.eh_depth == 0);

    struct ext4_extent ext = {
        .ee_block = 0,
        .ee_len = 128,
        .ee_start_hi = 0,
        .ee_start_lo = 204800
    };

    uint64_t physical_block = ((uint64_t)ext.ee_start_hi << 32) | ext.ee_start_lo;
    assert(physical_block == 204800);

    printf("dk_b19 verified successfully: Ext4 magic 0xF30A valid, physical block %llu mapped.\n",
           (unsigned long long)physical_block);
    return 0;
}
