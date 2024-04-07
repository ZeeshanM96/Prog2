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

    ns_1 = range(30, 46)
    times_py_1, times_numba_1, times_cpp_1 = [], [], []
    
    for n in ns_1:
        # Time Python version
        start = time.perf_counter()
        fib_py(n)
        times_py_1.append(time.perf_counter() - start)
        
        # Time Numba version
        start = time.perf_counter()
        fib_numba(n)
        times_numba_1.append(time.perf_counter() - start)
        
        # Time C++ version
        start = time.perf_counter()
        person = Person(n)  
        person.fib()
        times_cpp_1.append(time.perf_counter() - start)
    
    print("Python - Timings for n = 30 to 45: ")
    print(times_py_1)
    print("Numba - Timings for n = 30 to 45: ")
    print(times_numba_1)
    print("C++ - Timings for n = 30 to 45: ")
    print(times_cpp_1)
    
    ns_2 = range(20, 31)
    times_py_2, times_numba_2 = [], []
    
    for n in ns_2:
        # Time Python version
        start = time.perf_counter()
        fib_py(n)
        times_py_2.append(time.perf_counter() - start)
        
        # Time Numba version
        start = time.perf_counter()
        fib_numba(n)
        times_numba_2.append(time.perf_counter() - start)
        
    print("Python - Timings for n = 20 to 30: ")
    print(times_py_2)
    print("Numba - Timings for n = 20 to 30: ")
    print(times_numba_2)

    
    # Compute Fibonacci number for n = 47 using C++ and Numba
    fib_cpp_47 = Person(47).fib()
    fib_numba_47 = fib_numba(47)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    
    
    plt.subplot(2, 1, 1)
    plt.plot(ns_1, times_py_1, label='Python')
    plt.plot(ns_1, times_numba_1, label='Numba')
    plt.plot(ns_1, times_cpp_1, label='C++')
    plt.xlabel('Fibonacci Number n')
    plt.ylabel('Time (seconds)')
    plt.title('Timings for n = 30 to 45')
    plt.legend()
    
    
    plt.subplot(2, 1, 2)
    plt.plot(ns_2, times_py_2, label='Python')
    plt.plot(ns_2, times_numba_2, label='Numba')
    plt.xlabel('Fibonacci Number n')
    plt.ylabel('Time (seconds)')
    plt.title('Timings for n = 20 to 30')
    plt.legend()
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('fibonacci_timings.png')  # Save the plot
    
    # Print Fibonacci number for n = 47
    print("Fibonacci number for n = 47 (C++):", fib_cpp_47)
    print("Fibonacci number for n = 47 (Numba):", fib_numba_47)

if __name__ == '__main__':
    main()

# Fibonacci number for n = 47 (C++): -1323752223
# Fibonacci number for n = 47 (Numba): 2971215073

# Reason:
#     The difference in results is due to the computation or handling of large Fibonacci numbers. The negative
#  value obtained for the C++ computation tells us the potential overflow or underflow issues.
