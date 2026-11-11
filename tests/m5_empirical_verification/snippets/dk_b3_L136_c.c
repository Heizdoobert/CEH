#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
#include <string.h>
#include <errno.h>

#define NUM_WORKERS 4
#define MATRIX_ROWS 10000
#define MATRIX_COLS 100

static int32_t matrix[MATRIX_ROWS][MATRIX_COLS];
static int64_t global_grand_total = 0;
static pthread_mutex_t grand_total_mutex = PTHREAD_MUTEX_INITIALIZER;

typedef struct {
    int32_t worker_id;
    int32_t start_row;
    int32_t end_row;
    int64_t local_sum;
} worker_task_t;

void* worker_thread_entry(void* arg) {
    worker_task_t* task = (worker_task_t*)arg;
    int64_t accumulator = 0;

    for (int32_t r = task->start_row; r < task->end_row; ++r) {
        for (int32_t c = 0; c < MATRIX_COLS; ++c) {
            accumulator += matrix[r][c];
        }
    }
    task->local_sum = accumulator;

    /* Critical section protected by Mutex */
    pthread_mutex_lock(&grand_total_mutex);
    global_grand_total += accumulator;
    pthread_mutex_unlock(&grand_total_mutex);

    return NULL;
}

int main(void) {
    pthread_t threads[NUM_WORKERS];
    worker_task_t tasks[NUM_WORKERS];

    /* Initialize matrix with test data */
    for (int32_t r = 0; r < MATRIX_ROWS; ++r) {
        for (int32_t c = 0; c < MATRIX_COLS; ++c) {
            matrix[r][c] = 1; /* Total sum should equal MATRIX_ROWS * MATRIX_COLS = 1,000,000 */
        }
    }

    int32_t rows_per_worker = MATRIX_ROWS / NUM_WORKERS;

    for (int32_t i = 0; i < NUM_WORKERS; ++i) {
        tasks[i].worker_id = i;
        tasks[i].start_row = i * rows_per_worker;
        tasks[i].end_row = (i == NUM_WORKERS - 1) ? MATRIX_ROWS : (i + 1) * rows_per_worker;
        tasks[i].local_sum = 0;

        int rc = pthread_create(&threads[i], NULL, worker_thread_entry, &tasks[i]);
        if (rc != 0) {
            fprintf(stderr, "Error creating thread %d: %s\n", i, strerror(rc));
            exit(EXIT_FAILURE);
        }
    }

    for (int32_t i = 0; i < NUM_WORKERS; ++i) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&grand_total_mutex);

    printf("Calculated Grand Total: %lld (Expected: %lld)\n",
           (long long)global_grand_total,
           (long long)(MATRIX_ROWS * MATRIX_COLS));
    return 0;
}
