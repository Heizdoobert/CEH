#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5
#define LEFT  ((i + N - 1) % N)
#define RIGHT ((i + 1) % N)

enum { THINKING = 0, HUNGRY, EATING } state[N];
pthread_mutex_t phil_mutex = PTHREAD_MUTEX_INITIALIZER;
sem_t s[N]; /* One private semaphore per philosopher */

void test_philosopher(int i) {
    if (state[i] == HUNGRY && state[LEFT] != EATING && state[RIGHT] != EATING) {
        state[i] = EATING;
        sem_post(&s[i]); /* Unblock philosopher i */
    }
}

void take_forks(int i) {
    pthread_mutex_lock(&phil_mutex);
    state[i] = HUNGRY;
    test_philosopher(i);
    pthread_mutex_unlock(&phil_mutex);
    sem_wait(&s[i]); /* Wait until forks acquired */
}

void put_forks(int i) {
    pthread_mutex_lock(&phil_mutex);
    state[i] = THINKING;
    test_philosopher(LEFT);  /* Give left neighbor a chance to eat */
    test_philosopher(RIGHT); /* Give right neighbor a chance to eat */
    pthread_mutex_unlock(&phil_mutex);
}
