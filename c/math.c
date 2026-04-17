#include <stdio.h>

int suma(int a, int b) {
    return a + b;
}

int suma_wrapper(int a, int b) {
    return suma(a, b);
}
