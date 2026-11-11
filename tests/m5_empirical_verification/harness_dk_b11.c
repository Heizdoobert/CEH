#include <stdio.h>
#include <stdlib.h>
#include <stdatomic.h>
#include <pthread.h>
#include <assert.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b11_L658_c.c"

int main(void) {
    printf("Testing dk_b11: RCU Linked List Lookup...\n");

    /* Allocate and chain test nodes */
    struct rcu_node n3 = { .key = 30, .value = 300, .next = NULL };
    struct rcu_node n2 = { .key = 20, .value = 200, .next = &n3 };
    struct rcu_node n1 = { .key = 10, .value = 100, .next = &n2 };

    atomic_store_explicit(&g_head, &n1, memory_order_release);

    /* Lookups */
    assert(rcu_lookup(10) == 100);
    assert(rcu_lookup(20) == 200);
    assert(rcu_lookup(30) == 300);
    assert(rcu_lookup(40) == -1);

    printf("dk_b11 verified successfully: RCU lockless lookup returned expected values!\n");
    return 0;
}
