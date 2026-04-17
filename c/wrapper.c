#include <stdio.h>

extern long suma(long a, long b);
extern long resta(long a, long b);
extern long maximo(long a, long b);

long suma_wrapper(long a, long b) {
    return suma(a, b);
}

long resta_wrapper(long a, long b) {
    return resta(a, b);
}

long maximo_wrapper(long a, long b) {
    return maximo(a, b);
}

long suma_array(long* arr, long n);

long suma_array_wrapper(long* arr, long n) {
    return suma_array(arr, n);
}
