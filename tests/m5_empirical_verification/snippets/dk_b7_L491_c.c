#include <pthread.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

typedef struct {
    pthread_mutex_t lock;
    pthread_cond_t  read_cv;
    pthread_cond_t  write_cv;
    uint32_t active_readers;
    uint32_t active_writers;
    uint32_t waiting_writers;
} fair_rwlock_t;

void fair_rwlock_init(fair_rwlock_t *rw) {
    pthread_mutex_init(&rw->lock, NULL);
    pthread_cond_init(&rw->read_cv, NULL);
    pthread_cond_init(&rw->write_cv, NULL);
    rw->active_readers = 0;
    rw->active_writers = 0;
    rw->waiting_writers = 0;
}

void fair_rwlock_read_lock(fair_rwlock_t *rw) {
    pthread_mutex_lock(&rw->lock);
    /* Block if a writer is active or waiting (prevents writer starvation) */
    while (rw->active_writers > 0 || rw->waiting_writers > 0) {
        pthread_cond_wait(&rw->read_cv, &rw->lock);
    }
    rw->active_readers++;
    pthread_mutex_unlock(&rw->lock);
}

void fair_rwlock_read_unlock(fair_rwlock_t *rw) {
    pthread_mutex_lock(&rw->lock);
    rw->active_readers--;
    if (rw->active_readers == 0 && rw->waiting_writers > 0) {
        pthread_cond_signal(&rw->write_cv); /* Wake one waiting writer */
    }
    pthread_mutex_unlock(&rw->lock);
}

void fair_rwlock_write_lock(fair_rwlock_t *rw) {
    pthread_mutex_lock(&rw->lock);
    rw->waiting_writers++;
    /* Must wait until all active readers and writers finish */
    while (rw->active_readers > 0 || rw->active_writers > 0) {
        pthread_cond_wait(&rw->write_cv, &rw->lock);
    }
    rw->waiting_writers--;
    rw->active_writers = 1;
    pthread_mutex_unlock(&rw->lock);
}

void fair_rwlock_write_unlock(fair_rwlock_t *rw) {
    pthread_mutex_lock(&rw->lock);
    rw->active_writers = 0;
    if (rw->waiting_writers > 0) {
        pthread_cond_signal(&rw->write_cv);  /* Prioritize waiting writer */
    } else {
        pthread_cond_broadcast(&rw->read_cv); /* Wake all waiting readers */
    }
    pthread_mutex_unlock(&rw->lock);
}
