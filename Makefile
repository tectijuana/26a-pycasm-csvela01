all:
	gcc -g -c -fPIC asm/math.s -o math.o
	gcc -g -c -fPIC c/wrapper.c -o wrapper.o
	gcc -shared -o libmath.so math.o wrapper.o
