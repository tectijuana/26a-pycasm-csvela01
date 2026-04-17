import ctypes

lib = ctypes.CDLL("../libmath.so")

# Configurar funciones
lib.suma_wrapper.argtypes = [ctypes.c_long, ctypes.c_long]
lib.suma_wrapper.restype = ctypes.c_long

lib.resta_wrapper.argtypes = [ctypes.c_long, ctypes.c_long]
lib.resta_wrapper.restype = ctypes.c_long

lib.maximo_wrapper.argtypes = [ctypes.c_long, ctypes.c_long]
lib.maximo_wrapper.restype = ctypes.c_long

# Llamadas
print("Suma:", lib.suma_wrapper(5, 7))
print("Resta:", lib.resta_wrapper(10, 3))
print("Max:", lib.maximo_wrapper(8, 12))
# arreglo
import numpy as np

arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)

lib.suma_array_wrapper.argtypes = [ctypes.POINTER(ctypes.c_long), ctypes.c_long]
lib.suma_array_wrapper.restype = ctypes.c_long

resultado = lib.suma_array_wrapper(arr.ctypes.data_as(ctypes.POINTER(ctypes.c_long)), len(arr))

print("Suma array:", resultado)

import time
import numpy as np

# Crear arreglo grande
arr = np.arange(1, 1000000, dtype=np.int64)

# ---------- PYTHON ----------
inicio = time.time()
suma_py = sum(arr)
fin = time.time()

print("Python suma:", suma_py)
print("Tiempo Python:", fin - inicio)

# ---------- ASM ----------
inicio = time.time()

resultado = lib.suma_array_wrapper(
    arr.ctypes.data_as(ctypes.POINTER(ctypes.c_long)),
    len(arr)
)

fin = time.time()

print("ASM suma:", resultado)
print("Tiempo ASM:", fin - inicio)
