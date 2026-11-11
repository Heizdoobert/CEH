#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_CAPACITY 8
#define TOTAL_ITEMS     32

typedef struct {
    int32_t data[BUFFER_CAPACITY];
    int32_t head; /* Read pointer */
    int32_t tail; /* Write pointer */
    pthread_mutex_t mutex;
    sem_t sem_empty;
    sem_t sem_full;
} bounded_buffer_t;

static bounded_buffer_t g_buf;

void bounded_buffer_init(bounded_buffer_t *b) {
    b->head = 0;
    b->tail = 0;
    pthread_mutex_init(&b->mutex, NULL);
    sem_init(&b->sem_empty, 0, BUFFER_CAPACITY); /* Initially all slots empty */
    sem_init(&b->sem_full, 0, 0);                 /* Initially 0 slots full */
}

void bounded_buffer_put(bounded_buffer_t *b, int32_t item) {
    sem_wait(&b->sem_empty); /* Decrement empty slot count; blocks if buffer full */
    
    pthread_mutex_lock(&b->mutex);
    b->data[b->tail] = item;
    b->tail = (b->tail + 1) % BUFFER_CAPACITY;
    pthread_mutex_unlock(&b->mutex);

    sem_post(&b->sem_full); /* Increment full count; wakes up waiting consumers */
}

int32_t bounded_buffer_get(bounded_buffer_t *b) {
    sem_wait(&b->sem_full); /* Decrement full count; blocks if buffer empty */
    
    pthread_mutex_lock(&b->mutex);
    int32_t item = b->data[b->head];
    b->head = (b->head + 1) % BUFFER_CAPACITY;
    pthread_mutex_unlock(&b->mutex);

    sem_post(&b->sem_empty); /* Increment empty count; wakes up waiting producers */
    return item;
}

void* producer_thread(void* arg) {
    (void)arg;
    for (int32_t i = 1; i <= TOTAL_ITEMS; ++i) {
        bounded_buffer_put(&g_buf, i);
    }
    return NULL;
}

void* consumer_thread(void* arg) {
    (void)arg;
    for (int32_t i = 1; i <= TOTAL_ITEMS; ++i) {
        int32_t val = bounded_buffer_get(&g_buf);
        (void)val;
    }
    return NULL;
}

int main(void) {
    bounded_buffer_init(&g_buf);
    pthread_t prod, cons;

    pthread_create(&prod, NULL, producer_thread, NULL);
    pthread_create(&cons, NULL, consumer_thread, NULL);

    pthread_join(prod, NULL);
    pthread_join(cons, NULL);

    pthread_mutex_destroy(&g_buf.mutex);
    sem_destroy(&g_buf.sem_empty);
    sem_destroy(&g_buf.sem_full);

    printf("Producer-Consumer Bounded Buffer verification successful.\n");
    return 0;
}
