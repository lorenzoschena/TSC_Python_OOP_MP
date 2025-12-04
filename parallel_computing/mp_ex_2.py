"""
TSC 5.2 - Parallel Computing (Optimized for Lecture)
-----
This file contains the code for the parallel computing example in the TSC 5.2
class at the von Karman Institute for Fluid Dynamics.

authors:
- L. Schena, J. Christophe, F. Torres, J. Dominique and M. A. Mendez

AA 2024/25
"""
import multiprocessing as mp
from functools import partial
import time
import numpy as np
import matplotlib.pyplot as plt
import math

def heavy_computation(x, exponent):
    res = 0
    for _ in range(50):
        res += math.sin(x) ** exponent + math.cos(x) ** exponent
    return res

def power(x, exponent):
    return x ** exponent

def run_experiment():
    N = 5_000_000 
    data = range(N)
    exponent = 2
    
    # 2. Run Serial ONCE (Baseline)
    print("Running Serial...", end="", flush=True)
    t0 = time.time()
    # list(map(partial(power, exponent=exponent), data))
    list(map(partial(heavy_computation, exponent=exponent), data)) 
    t_serial = time.time() - t0
    print(f" Done ({t_serial:.2f}s)")

    # 3. Run Parallel for varying CPU counts
    cpus = mp.cpu_count()
    cpu_counts = range(1, cpus + 1)
    parallel_times = []

    print("Running Parallel scaling...", end="", flush=True)
    for n_proc in cpu_counts:
        t0 = time.time()
        # Important: Context manager ensures the pool closes immediately
        with mp.Pool(processes=n_proc) as pool:
            # pool.map(partial(power, exponent=exponent), data)
            pool.map(partial(heavy_computation, exponent=exponent), data) 
        t_parallel = time.time() - t0
        parallel_times.append(t_parallel)
        print(f".", end="", flush=True) # Progress dot
    
    print(" Done.")
    return t_serial, parallel_times, cpu_counts

if __name__ == "__main__":
    # Essential for macOS/Windows
    mp.set_start_method("spawn", force=True)
    
    # Run the experiment 3 times for statistics
    repeats = 2
    serial_results = []
    parallel_results = []
    
    print(f"Starting {repeats} experiment runs...")
    
    for i in range(repeats):
        print(f"\nRun {i+1}/{repeats}:")
        t_ser, t_par_list, cpu_range = run_experiment()
        serial_results.append(t_ser)
        parallel_results.append(t_par_list)

    # --- Plotting ---
    # Prepare data
    mean_serial = np.mean(serial_results)
    std_serial = np.std(serial_results)
    
    mean_parallel = np.mean(parallel_results, axis=0)
    std_parallel = np.std(parallel_results, axis=0)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.axhline(mean_serial, color='red', linestyle='--', label=f"Serial Avg ({mean_serial:.2f}s)")
    ax.fill_between(cpu_range, mean_serial - std_serial, mean_serial + std_serial, color='red', alpha=0.1)

    # Plot Parallel
    ax.errorbar(cpu_range, mean_parallel, yerr=std_parallel, 
                label="Parallel", marker='o', capsize=5, color="blue")

    ax.set_title("Scaling Performance: Serial vs Parallel")
    ax.set_xlabel("Number of Processes")
    ax.set_ylabel("Time [s]")
    ax.legend()
    ax.grid(True, which="both", ls="-", alpha=0.5)
    
    plt.tight_layout()
    plt.show()