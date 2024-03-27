#!/usr/bin/env python3.9
import time
from person import Person
from numba import jit
import matplotlib.pyplot as plt

# Pure Python Fibonacci
def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n-1) + fib_py(n-2)

# Numba-optimized Fibonacci
@jit(nopython=True)
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)

def main():
    ns = range(30, 46)  # Adjust as needed
    times_py, times_numba, times_cpp = [], [], []
    
    for n in ns:
        # Time Python version
        start = time.perf_counter()
        fib_py(n)
        times_py.append(time.perf_counter() - start)
        
        # Time Numba version
        start = time.perf_counter()
        fib_numba(n)
        times_numba.append(time.perf_counter() - start)
        
        # Time C++ version
        start = time.perf_counter()
        person = Person(n)  # Assumes Person class is already linked to fib method
        person.fib()
        times_cpp.append(time.perf_counter() - start)
    
    # Plotting
    plt.figure()
    plt.plot(ns, times_py, label='Python')
    plt.plot(ns, times_numba, label='Numba')
    plt.plot(ns, times_cpp, label='C++')
    plt.xlabel('Fibonacci Number n')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.savefig('fibonacci_timings.png')  # Save the plot

if __name__ == '__main__':
    main()
