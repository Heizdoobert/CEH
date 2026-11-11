/* Vulnerable C code */
#include <string.h>

void vulnerable_function(const char *untrusted_input) {
    char buffer[64];
    strcpy(buffer, untrusted_input); /* Unsafe: no boundary check! */
}

/* Equivalent assembly emitted by GCC with Stack Canary */
/*
vulnerable_function:
    subq    $88, %rsp
    movq    %fs:40, %rax          ; Load canary from Thread Local Storage
    movq    %rax, 72(%rsp)        ; Store canary directly below saved RBP
    xorl    %eax, %eax
    ...
    ; Function body executes here
    ...
    movq    72(%rsp), %rax
    xorq    %fs:40, %rax          ; Verify canary integrity
    jne     .stack_smash_failed   ; If altered, jump to abort!
    addq    $88, %rsp
    ret
.stack_smash_failed:
    call    __stack_chk_fail      ; Abort process immediately
*/
