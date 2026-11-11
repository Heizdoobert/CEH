semaphore mutex = 1;       // Protects read_count
semaphore resource = 1;    // Exclusive access to shared resource
semaphore queue_order = 1; // FIFO arrival turnstile
int read_count = 0;

// --- Reader Process ---
void reader() {
    wait(queue_order);     // Step in the FIFO queue
    wait(mutex);           // Protect read_count
    read_count++;
    if (read_count == 1) {
        wait(resource);    // First reader locks the resource against writers
    }
    signal(mutex);
    signal(queue_order);   // Release queue turnstile for next arriver

    // [CRITICAL SECTION: Reading shared data]
    perform_reading();

    wait(mutex);
    read_count--;
    if (read_count == 0) {
        signal(resource);  // Last reader releases resource for waiting writers
    }
    signal(mutex);
}

// --- Writer Process ---
void writer() {
    wait(queue_order);     // Step in the FIFO queue
    wait(resource);        // Wait for active readers/writers to finish
    signal(queue_order);   // Release queue turnstile

    // [CRITICAL SECTION: Modifying shared data]
    perform_writing();

    signal(resource);      // Release resource
}
