#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <assert.h>
#include <unistd.h>

/* Implement semaphore as int with monitor-based wait/signal for textbook pseudo-C */
typedef int semaphore;

static pthread_mutex_t g_sem_mutex = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t g_sem_cv = PTHREAD_COND_INITIALIZER;

static void textbook_wait(semaphore *s) {
    pthread_mutex_lock(&g_sem_mutex);
    while (*s <= 0) {
        pthread_cond_wait(&g_sem_cv, &g_sem_mutex);
    }
    (*s)--;
    pthread_mutex_unlock(&g_sem_mutex);
}

static void textbook_signal(semaphore *s) {
    pthread_mutex_lock(&g_sem_mutex);
    (*s)++;
    pthread_cond_broadcast(&g_sem_cv);
    pthread_mutex_unlock(&g_sem_mutex);
}

#define wait(s) textbook_wait(&(s))
#define signal(s) textbook_signal(&(s))

static volatile int active_readers = 0;
static volatile int active_writers = 0;
static int shared_data = 0;
static int total_reads = 0;
static int total_writes = 0;
static pthread_mutex_t verify_lock = PTHREAD_MUTEX_INITIALIZER;

void perform_reading(void) {
    pthread_mutex_lock(&verify_lock);
    active_readers++;
    assert(active_writers == 0); /* Mutual exclusion invariant */
    total_reads++;
    pthread_mutex_unlock(&verify_lock);

    int val = shared_data;
    (void)val;

    pthread_mutex_lock(&verify_lock);
    active_readers--;
    pthread_mutex_unlock(&verify_lock);
}

void perform_writing(void) {
    pthread_mutex_lock(&verify_lock);
    active_writers++;
    assert(active_writers == 1); /* Strict exclusive write invariant */
    assert(active_readers == 0); /* No readers during write */
    shared_data++;
    total_writes++;
    pthread_mutex_unlock(&verify_lock);

    pthread_mutex_lock(&verify_lock);
    active_writers--;
    pthread_mutex_unlock(&verify_lock);
}

/* Include textbook snippet */
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/eq_b6_L1423_c.c"

#define NUM_READERS 6
#define NUM_WRITERS 3
#define OPS 100

void* reader_thread(void* arg) {
    (void)arg;
    for (int i = 0; i < OPS; ++i) {
        reader();
    }
    return NULL;
}

void* writer_thread(void* arg) {
    (void)arg;
    for (int i = 0; i < OPS; ++i) {
        writer();
    }
    return NULL;
}

int main(void) {
    printf("Testing eq_b6: Fair Readers-Writers with FIFO Turnstile (Exam Bank)...\n");

    pthread_t r_threads[NUM_READERS];
    pthread_t w_threads[NUM_WRITERS];

    for (int i = 0; i < NUM_READERS; ++i) pthread_create(&r_threads[i], NULL, reader_thread, NULL);
    for (int i = 0; i < NUM_WRITERS; ++i) pthread_create(&w_threads[i], NULL, writer_thread, NULL);

    for (int i = 0; i < NUM_READERS; ++i) pthread_join(r_threads[i], NULL);
    for (int i = 0; i < NUM_WRITERS; ++i) pthread_join(w_threads[i], NULL);

    printf("eq_b6 verified successfully: total_reads=%d, total_writes=%d, shared_data=%d\n",
           total_reads, total_writes, shared_data);
    assert(total_reads == NUM_READERS * OPS);
    assert(total_writes == NUM_WRITERS * OPS);
    assert(shared_data == NUM_WRITERS * OPS);
    return 0;
}
