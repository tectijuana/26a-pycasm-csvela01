.global suma
.global resta
.global maximo

// long suma(long a, long b)
suma:
    add x0, x0, x1
    ret

// long resta(long a, long b)
resta:
    sub x0, x0, x1
    ret

// long maximo(long a, long b)
maximo:
    cmp x0, x1
    bge .return_a
    mov x0, x1
.return_a:
    ret
.global suma_array

// long suma_array(long* arr, long n)
suma_array:
    mov x2, #0      // i = 0
    mov x3, #0      // suma = 0

.loop:
    cmp x2, x1
    bge .fin

    ldr x4, [x0, x2, LSL #3]   // arr[i]
    add x3, x3, x4

    add x2, x2, #1
    b .loop

.fin:
    mov x0, x3
    ret
