#define _DEFAULT_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
#include <semaphore.h>
#include <assert.h>
#include <unistd.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b8_L566_c.c"

#define MEALS_PER_PHIL 50

static int meals_eaten[N] = {0};

void* philosopher_worker(void* arg) {
    int id = (int)(intptr_t)arg;
    for (int m = 0; m < MEALS_PER_PHIL; ++m) {
        /* Think */
        usleep(100);

        take_forks(id);

        /* Eat: verify neighbors are NOT eating */
        pthread_mutex_lock(&phil_mutex);
        assert(state[id] == EATING);
        assert(state[(id + 1) % N] != EATING);
        assert(state[(id + N - 1) % N] != EATING);
        meals_eaten[id]++;
        pthread_mutex_unlock(&phil_mutex);

        usleep(200);

        put_forks(id);
    }
    return NULL;
}

int main(void) {
    printf("Testing dk_b8: Tanenbaum Dining Philosophers...\n");
    pthread_t phils[N];

    for (int i = 0; i < N; ++i) {
        sem_init(&s[i], 0, 0);
        state[i] = THINKING;
    }

    for (int i = 0; i < N; ++i) {
        pthread_create(&phils[i], NULL, philosopher_worker, (void*)(intptr_t)i);
    }

    for (int i = 0; i < N; ++i) {
        pthread_join(phils[i], NULL);
    }

    for (int i = 0; i < N; ++i) {
        printf("  Philosopher %d ate %d meals.\n", i, meals_eaten[i]);
        assert(meals_eaten[i] == MEALS_PER_PHIL);
        sem_destroy(&s[i]);
    }

    printf("dk_b8 verified successfully: No deadlock, strict mutual exclusion between neighbors!\n");
    return 0;
}
