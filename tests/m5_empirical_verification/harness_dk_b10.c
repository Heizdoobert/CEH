#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdbool.h>
#include <assert.h>
#include <unistd.h>

static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
static bool work_available = false;
static int work_item = 0;

void* worker(void* arg) {
    (void)arg;
    #include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b10_L636_c.c"
    return NULL;
}

int main(void) {
    printf("Testing dk_b10: Condition Variable While-Loop Idiom...\n");
    pthread_t t;
    pthread_create(&t, NULL, worker, NULL);

    usleep(50000); /* 50ms wait */

    pthread_mutex_lock(&mutex);
    work_item = 42;
    work_available = true;
    pthread_cond_signal(&cv);
    pthread_mutex_unlock(&mutex);

    pthread_join(t, NULL);

    printf("dk_b10 verified successfully: Handled condition variable wait and wake-up cleanly!\n");
    return 0;
}
