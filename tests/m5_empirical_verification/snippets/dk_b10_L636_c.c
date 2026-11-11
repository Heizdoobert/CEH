pthread_mutex_lock(&mutex);
while (!work_available) {          /* MANDATORY WHILE LOOP */
    pthread_cond_wait(&cv, &mutex);
}
// process work...
pthread_mutex_unlock(&mutex);
