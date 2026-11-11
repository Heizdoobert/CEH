// Shared global state variables
int turn;               // Whose turn is it to enter?
bool flag[2] = {false, false}; // flag[i] = true means Process i wants to enter

// Process i (where i = 0 or 1, and other process is j = 1 - i)
void enter_region(int i) {
    int j = 1 - i;
    flag[i] = true;          // Declare intent to enter
    turn = j;                // Generously yield priority to other process
    // Busy wait as long as the other wants to enter AND it is the other's turn
    while (flag[j] == true && turn == j) {
        // spinlock wait
    }
}

void leave_region(int i) {
    flag[i] = false;         // Relinquish access
}
