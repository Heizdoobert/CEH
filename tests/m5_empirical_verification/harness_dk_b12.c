#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b12_L762_c.c"

int main(void) {
    printf("Testing dk_b12: Linux Kernel CFS Weight Table (sched_prio_to_weight)...\n");

    /* Total size should be 40 ints */
    size_t count = sizeof(sched_prio_to_weight) / sizeof(sched_prio_to_weight[0]);
    assert(count == 40);

    /* nice = -20 (index 0) */
    assert(sched_prio_to_weight[0] == 88761);

    /* nice = 0 (index 20) -> NICE_0_LOAD = 1024 */
    assert(sched_prio_to_weight[20] == 1024);

    /* nice = +19 (index 39) */
    assert(sched_prio_to_weight[39] == 15);

    /* Check geometric ratio ~ 1.25 across adjacent levels */
    double min_ratio = 10.0, max_ratio = 0.0;
    for (size_t i = 0; i < count - 1; ++i) {
        double ratio = (double)sched_prio_to_weight[i] / (double)sched_prio_to_weight[i + 1];
        if (ratio < min_ratio) min_ratio = ratio;
        if (ratio > max_ratio) max_ratio = ratio;
        /* Ratios should be strictly within [1.18, 1.30] */
        assert(ratio >= 1.18 && ratio <= 1.30);
    }

    printf("dk_b12 verified successfully: count=%zu, nice_0=1024, ratio_range=[%.3f, %.3f] ~ 1.25\n",
           count, min_ratio, max_ratio);
    return 0;
}
