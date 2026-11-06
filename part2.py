# -*- coding: utf-8 -*-

"""
Arina Basai 

"""

import random
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter


"Given functions"

def generate_rnd_array1(n, vmax=1000):
    x = np.zeros(n)
    for i in range(n):
        x[i] = random.randint(0, vmax)*0.01*i
    return x

def generate_rnd_array2(n, vmax=1000):
    x = np.zeros(n)
    for i in range(n):
        x[i] = i + 10*np.sin(2*np.pi*0.01)*random.randint(0, vmax)
    return x

"My functions"

"Function 1"
  
def sample_array(arr: np.ndarray, n: int):
    """
    Creates a new array of samples from the input array

    Parameters
    ----------
    arr : np.ndarray
        an array from which samples are derived
    n : int
        quantity of random samples.

    Returns
    -------
    samples : np.ndarray
        array with n random samples

    """
    if 0 < n <= len(arr):
        samples = np.ones((n, ), dtype = arr.dtype)
        index_counter = []
        s = 0
        while s < n:
            i = random.randint(0, len(arr) - 1)
            if i not in index_counter:
                samples[s] = arr[i]
                index_counter.append(i)
                s += 1
        return samples
    else:
        return None
    
def sort_array(arr: np.ndarray):
    """
    Sorts an array using recursive Quicksort algorithm (Divide and Conquer)

    Parameters
    ----------
    arr : np.ndarray
        an array to be sorted

    Returns
    -------
    np.ndarray: a sorted array

    """
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    first_half = arr[arr < pivot]
    pivot_if_repetition = arr[arr == pivot]
    second_half = arr[arr > pivot]
    return np.concatenate((sort_array(first_half), pivot_if_repetition, sort_array(second_half)))

def average_time(data: np.ndarray, n: int):
    """
    Computes the average time sort_array takes out of n repetitions

    Parameters
    ----------
    data : np.ndarray
        an array to be sorted
    n : int
        the number of repetitions

    Returns
    -------
    av_time: float
        the average time
        
    """
    total_time = 0
    for i in range(n):
        copied_data = data.copy()
        start = perf_counter()
        sort_array(copied_data)
        stop = perf_counter()
        total_time += (stop - start)
    av_time = total_time/n
    return av_time
    
def estimate_complexity(data: np.ndarray, n_samples: np.ndarray):
    """
    Used for plotting and analysing complexity of the sort_array function

    Parameters
    ----------
    data : np.ndarray
        an array to be sorted
    n_samples : np.ndarray
        sample array

    Returns
    -------
    complexity: np.ndarray
        an array with the shape of n_samples and elements corresponding to average time

    """
    complexity = []
    for n in n_samples:
        subset = data[:n]
        av_time = average_time(subset, 10)
        complexity.append(av_time)
    return np.array(complexity)

def main():
    
    "Graph 1:"
    ar1 = generate_rnd_array1(1000)
    ar2 = generate_rnd_array2(1000)
    plt.figure(figsize = (15, 12))
    plt.subplot(3, 1, 1)
    plt.plot(ar1, label = "Original Array 1")
    plt.plot(ar2, label = "Original Array 1")
    plt.title("Originals")
    plt.legend()
    
    "Graph 2:"
    ar1_sorted = sort_array(ar1)
    ar2_sorted = sort_array(ar2)
    plt.subplot(3, 1, 2)
    plt.plot(ar1_sorted, label = "Sorted Array 1")
    plt.plot( ar2_sorted, label = "Sorted Array 2")
    plt.title("Sorted")
    plt.legend()
    
    "Graph 3:"
    n_samples = [10 + i*20 for i in range((len(ar1) - 10) // 20 + 1)]
    complexity_1 = estimate_complexity(ar1, n_samples)
    complexity_2 = estimate_complexity(ar2, n_samples)
    plt.subplot(3, 1, 3)
    plt.plot(n_samples, complexity_1, label = "Processing time arr1", marker = "o")
    plt.plot(n_samples, complexity_2, label = "Processing time arr2", marker = "o")
    plt.xlabel("Number of samples")
    plt.ylabel("Average Processing Time")
    plt.title("Complexity")
    plt.legend()
    plt.show()
    return

if __name__ == "__main__":
    main()
    
    
    
    