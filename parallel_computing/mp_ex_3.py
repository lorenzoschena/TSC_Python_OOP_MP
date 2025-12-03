"""
TSC 5.2 - Parallel Computing
-----
Example 3: The "Production" Pattern.
Connecting Classes (Structure) with Multiprocessing (Scale).

Key concepts:
1. Using Objects to package parameters (avoiding complex 'starmap'/'partial' calls).
2. Using 'imap' + 'tqdm' to show a progress bar.
"""
import multiprocessing as mp
import time
import random
from dataclasses import dataclass
from tqdm import tqdm  # pip install tqdm

# --- PART 1: The "Job" Object (OOP) ---

@dataclass
class WindTunnelTest:
    id: int
    velocity: float
    angle_of_attack: float
    
    def __call__(self):
        """
        The logic to be executed on the worker.
        """
        # 1. Simulate setup overhead
        time.sleep(random.uniform(0.5, 1.5)) 
        
        noise = random.normalvariate(0, 0.05)
        drag = 0.5 * 1.225 * (self.velocity**2) * 0.1 * (1 + 0.01*self.angle_of_attack)
        
        return f"Test {self.id:02d}: V={self.velocity}m/s, Alpha={self.angle_of_attack}deg -> Drag={drag:.2f}N"

# Helper function to unpack and run the object
# (Top-level functions are easiest to pickle)
def run_job(job):
    return job()

def main():
    print("--- Preparing Batch Simulation ---")
    
    # 1. Create a list of DISTINCT jobs (The OOP Advantage)
    # Notice how easy it is to manage different parameters for each job.
    tests = [
        WindTunnelTest(id=i, velocity=10 + i, angle_of_attack=i/2) 
        for i in range(20)
    ]
    
    print(f"Created {len(tests)} unique test cases.")
    
    # 2. Parallel Execution with Progress Bar
    print("\n--- Starting Workers ---")
    
    results = []
    t0 = time.time()
    
    with mp.Pool() as pool:
        iterator = pool.imap_unordered(run_job, tests)
        
        for res in tqdm(iterator, total=len(tests)):
            results.append(res)
            
    print(f"\nDone! Total time: {time.time() - t0:.2f}s")

    print("\nSample Results:")
    for r in results[:3]:
        print(r)

if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    main()