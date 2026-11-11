#include <stdio.h>
#include <stdlib.h>
#include <stdatomic.h>

struct rcu_node {
    int key;
    int value;
    struct rcu_node *next;
};

/* Global pointer protected by RCU mechanics */
_Atomic(struct rcu_node*) g_head = NULL;

/* Reader-side: Zero locking overhead */
int rcu_lookup(int target_key) {
    /* Read head atomically with acquire semantics */
    struct rcu_node *curr = atomic_load_explicit(&g_head, memory_order_consume);
    while (curr != NULL) {
        if (curr->key == target_key) {
            return curr->value;
        }
        curr = curr->next;
    }
    return -1; /* Not found */
}
