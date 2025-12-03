"""
TSC 5.2 - Parallel Computing
-----
This file contains the code for the parallel computing example in the TSC 5.2
class at the von Karman Institute for Fluid Dynamics.

authors:
- L. Schena, J. Christophe, F. Torres, J. Dominique and M. A. Mendez

AA 2024/25
"""
import numpy as np
import datetime
import multiprocessing as mp

print("Number of processors: ", mp.cpu_count())


def worker(_):
    """worker function"""
    print('Worker called! {}'.format(datetime.datetime.now().strftime("%H:%M:%S")))
    return True


if __name__ == '__main__':
    # On macOS, the default start method is 'fork' which is not compatible with the multiprocessing module
    mp.set_start_method('spawn', force=True)

    with mp.Pool() as pool:
        results = pool.map(worker, range(10))

