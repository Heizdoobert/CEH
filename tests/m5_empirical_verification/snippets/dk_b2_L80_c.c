#include <stdint.h>
#include <stdbool.h>
#include <sys/types.h>

/* Register state saved on the kernel stack during x86-64 context switch */
struct pcb_context {
    uint64_t r15;
    uint64_t r14;
    uint64_t r13;
    uint64_t r12;
    uint64_t rbp;
    uint64_t rbx;
    uint64_t rip;    /* Return instruction pointer */
    uint64_t rsp;    /* Kernel stack pointer */
    uint64_t rflags;
};

/* Process states matching POSIX / Tanenbaum lifecycle */
enum process_state {
    TASK_RUNNING = 0,         /* Currently executing or in ready queue */
    TASK_INTERRUPTIBLE,       /* Blocked waiting for an event/signal */
    TASK_UNINTERRUPTIBLE,     /* Blocked waiting for hardware I/O */
    TASK_STOPPED,             /* Execution suspended by SIGSTOP */
    TASK_ZOMBIE               /* Terminated, PCB retained for parent wait() */
};

/* Architectural simulation of Process Control Block (task_struct) */
struct task_struct_sim {
    pid_t                     pid;              /* Unique Process Identifier */
    pid_t                     tgid;             /* Thread Group ID (POSIX PID) */
    enum process_state        state;            /* Execution state */
    uint64_t                  vruntime;         /* Virtual runtime for CFS */
    int32_t                   prio;             /* Dynamic priority */
    int32_t                   static_prio;      /* Static nice priority (-20..19) */
    struct pcb_context        context;          /* Saved hardware registers */
    void                     *kernel_stack;     /* Pointer to 8KB/16KB kernel stack */
    uint64_t                  cr3_pgd;          /* Physical address of PML4 (Page Table Root) */
    uint32_t                  open_fds_count;   /* Count of open file descriptors */
    struct task_struct_sim   *parent;           /* Pointer to parent process */
};
