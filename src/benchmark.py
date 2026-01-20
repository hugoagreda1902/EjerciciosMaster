import time
import numpy as np
from numba import njit

N = 10_000_000   # 10 millones

# =========================
# VERSIONES A COMPARAR
# =========================

# --- A: Python puro ---
def version_python(x):
    m = sum(x) / len(x)
    total = 0.0
    for i in x:
        total += (i - m) ** 2
    return total


# --- B: NumPy vectorizado ---
def version_numpy(x):
    m = np.mean(x)
    return np.sum((x - m) ** 2)


# --- C: Numba compilado ---
@njit
def version_numba(x):
    m = x.mean()
    total = 0.0
    for i in x:
        total += (i - m) ** 2
    return total


# =========================
# UTILIDADES
# =========================

def medir(func, data):
    tiempos = []
    for _ in range(3):
        inicio = time.perf_counter()
        func(data)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / len(tiempos)


def ejecutar_bench(dtype):

    print(f"\n===== BENCHMARK con {dtype} =====")

    # Datos
    datos_python = [float(i) for i in range(N)]
    datos_numpy = np.array(datos_python, dtype=dtype)

    # Warmup para numba
    version_numba(datos_numpy)

    t_python = medir(version_python, datos_python)
    t_numpy  = medir(version_numpy, datos_numpy)
    t_numba  = medir(version_numba, datos_numpy)

    print(f"Python puro : {t_python:.4f} s")
    print(f"NumPy       : {t_numpy:.4f} s")
    print(f"Numba       : {t_numba:.4f} s")

    print("\nRatios:")
    print(f"NumPy vs Python : x{t_python/t_numpy:.1f}")
    print(f"Numba vs Python : x{t_python/t_numba:.1f}")
    print(f"Numba vs NumPy  : x{t_numpy/t_numba:.1f}")


def main():
    print("Generando benchmarks...")
    ejecutar_bench(np.float64)
    ejecutar_bench(np.float32)


if __name__ == "__main__":
    main()
