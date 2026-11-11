#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b2_L80_c.c"

int main(void) {
    printf("Testing dk_b2: struct task_struct_sim...\n");

    struct task_struct_sim t;
    t.pid = 1001;
    t.tgid = 1001;
    t.state = TASK_RUNNING;
    t.vruntime = 150000;
    t.prio = 120;
    t.static_prio = 0;
    t.kernel_stack = (void*)0xFFFF888000000000ULL;
    t.cr3_pgd = 0x1000000ULL;
    t.open_fds_count = 3;
    t.parent = NULL;

    t.context.rip = 0x401000;
    t.context.rsp = 0x7FFFFFFFDE00;
    t.context.rflags = 0x202;

    assert(t.pid == 1001);
    assert(t.state == TASK_RUNNING);
    assert(t.vruntime == 150000);
    assert(t.context.rip == 0x401000);

    printf("dk_b2 verified successfully: sizeof(task_struct_sim) = %zu bytes\n", sizeof(struct task_struct_sim));
    return 0;
}
