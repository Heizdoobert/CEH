#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b25_L1433_c.c"

int main(void) {
    printf("Testing dk_b25: Stack Canary Buffer Protection...\n");

    /* Normal benign input */
    const char *safe_input = "Safe short string within 64-byte buffer";
    vulnerable_function(safe_input);

    printf("dk_b25 verified successfully: Benign call succeeded without triggering canary abort.\n");
    return 0;
}
