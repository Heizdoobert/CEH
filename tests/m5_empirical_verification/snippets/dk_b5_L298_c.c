#include <stdatomic.h>
#include <stdbool.h>
#include <stdint.h>

atomic_bool peterson_flag[2] = {false, false};
atomic_int  peterson_turn = 0;

void peterson_enter(int self) {
    int other = 1 - self;
    atomic_store_explicit(&peterson_flag[self], true, memory_order_seq_cst);
    atomic_store_explicit(&peterson_turn, other, memory_order_seq_cst);

    /* Full hardware memory barrier enforced by sequential consistency */
    while (atomic_load_explicit(&peterson_flag[other], memory_order_seq_cst) &&
           atomic_load_explicit(&peterson_turn, memory_order_seq_cst) == other) {
        #if defined(__x86_64__) || defined(_M_X64)
        __builtin_ia32_pause(); /* Emit PAUSE instruction to prevent CPU pipeline starvation */
        #endif
    }
}

void peterson_leave(int self) {
    atomic_store_explicit(&peterson_flag[self], false, memory_order_seq_cst);
}
