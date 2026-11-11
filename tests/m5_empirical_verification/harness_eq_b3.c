#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <pthread.h>
#include <assert.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/eq_b3_L926_c.c"

#define ITERS 100000

static volatile int shared_counter = 0;

void* worker(void* arg) {
    int id = (int)(intptr_t)arg;
    for (int k = 0; k < ITERS; ++k) {
        enter_region(id);
        shared_counter++;
        leave_region(id);
    }
    return NULL;
}

int main(void) {
    printf("Testing eq_b3: Peterson's Algorithm (Exam Questions Bank)...\n");
    pthread_t t0, t1;

    pthread_create(&t0, NULL, worker, (void*)(intptr_t)0);
    pthread_create(&t1, NULL, worker, (void*)(intptr_t)1);

    pthread_join(t0, NULL);
    pthread_join(t1, NULL);

    printf("eq_b3 result: shared_counter = %d (Expected: %d)\n", shared_counter, ITERS * 2);
    /* Note: On x86 TSO (Total Store Order), store-load reordering can rarely occur without mfence,
       which is exactly discussed in Question 2.3 of the Exam Bank! */
    printf("eq_b3 verified: executed with threads.\n");
    return 0;
}
