#include <stdint.h>

/* Ext4 on-disk extent tree header */
struct ext4_extent_header {
    uint16_t eh_magic;      /* Magic number: 0xF30A */
    uint16_t eh_entries;    /* Number of valid entries following header */
    uint16_t eh_max;        /* Capacity of entries in this node */
    uint16_t eh_depth;      /* 0 = leaf node pointing to data, >0 = index node */
    uint32_t eh_generation; /* Generation of the tree */
};

/* Ext4 leaf node extent: describes contiguous disk allocation */
struct ext4_extent {
    uint32_t ee_block;      /* First logical file block covered by extent */
    uint16_t ee_len;        /* Number of blocks (up to 32,768) */
    uint16_t ee_start_hi;   /* High 16 bits of physical block address */
    uint32_t ee_start_lo;   /* Low 32 bits of physical block address */
};
