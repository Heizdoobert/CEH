#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <assert.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b5_L298_c.c"

#define ITERS 200000

static volatile int64_t shared_counter = 0;

void* thread_func(void* arg) {
    int self = (int)(intptr_t)arg;
    for (int i = 0; i < ITERS; ++i) {
        peterson_enter(self);
        /* Critical section: single writer guaranteed */
        shared_counter++;
        peterson_leave(self);
    }
    return NULL;
}

int main(void) {
    printf("Testing dk_b5: Peterson's Algorithm with C11 Atomics...\n");
    pthread_t t0, t1;

    pthread_create(&t0, NULL, thread_func, (void*)(intptr_t)0);
    pthread_create(&t1, NULL, thread_func, (void*)(intptr_t)1);

    pthread_join(t0, NULL);
    pthread_join(t1, NULL);

    printf("dk_b5 result: shared_counter = %lld (Expected: %lld)\n",
           (long long)shared_counter, (long long)(ITERS * 2));
    assert(shared_counter == ITERS * 2);
    printf("dk_b5 verified successfully: 100%% Mutual Exclusion under heavy contention!\n");
    return 0;
}
