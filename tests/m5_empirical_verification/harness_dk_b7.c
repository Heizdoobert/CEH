#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <assert.h>
#include <unistd.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b7_L491_c.c"

#define NUM_READERS 8
#define NUM_WRITERS 4
#define OPS_PER_THREAD 500

static fair_rwlock_t rwlock;
static int shared_resource = 0;
static volatile int readers_in_cs = 0;
static volatile int writers_in_cs = 0;
static int total_reads = 0;
static int total_writes = 0;
static pthread_mutex_t stats_lock = PTHREAD_MUTEX_INITIALIZER;

void* reader_worker(void* arg) {
    (void)arg;
    for (int i = 0; i < OPS_PER_THREAD; ++i) {
        fair_rwlock_read_lock(&rwlock);
        
        __atomic_fetch_add(&readers_in_cs, 1, __ATOMIC_SEQ_CST);
        assert(__atomic_load_n(&writers_in_cs, __ATOMIC_SEQ_CST) == 0);
        
        int val = shared_resource;
        (void)val;
        
        __atomic_fetch_sub(&readers_in_cs, 1, __ATOMIC_SEQ_CST);
        fair_rwlock_read_unlock(&rwlock);

        pthread_mutex_lock(&stats_lock);
        total_reads++;
        pthread_mutex_unlock(&stats_lock);
    }
    return NULL;
}

void* writer_worker(void* arg) {
    (void)arg;
    for (int i = 0; i < OPS_PER_THREAD; ++i) {
        fair_rwlock_write_lock(&rwlock);
        
        __atomic_fetch_add(&writers_in_cs, 1, __ATOMIC_SEQ_CST);
        assert(__atomic_load_n(&writers_in_cs, __ATOMIC_SEQ_CST) == 1);
        assert(__atomic_load_n(&readers_in_cs, __ATOMIC_SEQ_CST) == 0);
        
        shared_resource++;
        
        __atomic_fetch_sub(&writers_in_cs, 1, __ATOMIC_SEQ_CST);
        fair_rwlock_write_unlock(&rwlock);

        pthread_mutex_lock(&stats_lock);
        total_writes++;
        pthread_mutex_unlock(&stats_lock);
    }
    return NULL;
}

int main(void) {
    printf("Testing dk_b7: Fair RWLock (Writer-Preference & Anti-Starvation)...\n");
    fair_rwlock_init(&rwlock);

    pthread_t readers[NUM_READERS];
    pthread_t writers[NUM_WRITERS];

    for (int i = 0; i < NUM_READERS; ++i) pthread_create(&readers[i], NULL, reader_worker, NULL);
    for (int i = 0; i < NUM_WRITERS; ++i) pthread_create(&writers[i], NULL, writer_worker, NULL);

    for (int i = 0; i < NUM_READERS; ++i) pthread_join(readers[i], NULL);
    for (int i = 0; i < NUM_WRITERS; ++i) pthread_join(writers[i], NULL);

    printf("dk_b7 verified successfully: Total reads=%d, Total writes=%d, Final resource=%d\n",
           total_reads, total_writes, shared_resource);
    assert(total_reads == NUM_READERS * OPS_PER_THREAD);
    assert(total_writes == NUM_WRITERS * OPS_PER_THREAD);
    assert(shared_resource == NUM_WRITERS * OPS_PER_THREAD);
    return 0;
}
