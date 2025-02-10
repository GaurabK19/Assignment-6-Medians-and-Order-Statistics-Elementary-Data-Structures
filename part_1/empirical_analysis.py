import random
import time
import numpy as np
import matplotlib.pyplot as plt

def median_of_medians(arr, k):
    """
    Deterministic Selection Algorithm (Median of Medians)
    Finds the k-th smallest element in the array using worst-case O(n) complexity.
    """
    if not arr:
        raise ValueError("Array is empty")
    if k < 0 or k >= len(arr):
        raise ValueError("Invalid k value")
    
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide into groups of 5 and find medians
    chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]

    # Step 2: Recursively find the median of medians
    pivot = median_of_medians(medians, len(medians)//2)

    # Step 3: Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = len([x for x in arr if x == pivot])

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - count)


def quickselect(arr, k):
    """
    Randomized Quickselect Algorithm
    Finds the k-th smallest element in the array with an expected O(n) time complexity.
    """
    if not arr:
        raise ValueError("Array is empty")
    if k < 0 or k >= len(arr):
        raise ValueError("Invalid k value")

    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = len([x for x in arr if x == pivot])

    if k < len(low):
        return quickselect(low, k)
    elif k < len(low) + count:
        return pivot
    else:
        return quickselect(high, k - len(low) - count)


def measure_time(func, arr, k):
    """
    Measures execution time of a function.
    """
    start_time = time.time()
    result = func(arr.copy(), k)
    end_time = time.time()
    return result, end_time - start_time


def generate_test_data(size, distribution):
    """
    Generates test data based on the given distribution type.
    """
    if distribution == "random":
        return np.random.randint(0, 100000, size).tolist()
    elif distribution == "sorted":
        return list(range(size))
    elif distribution == "reverse_sorted":
        return list(range(size, 0, -1))


# Define test sizes and distributions
sizes = [100, 500, 1000, 5000, 10000, 20000]
distributions = ["random", "sorted", "reverse_sorted"]

results = {"Deterministic": {}, "Randomized": {}}

# Run empirical analysis for each distribution
for dist in distributions:
    results["Deterministic"][dist] = []
    results["Randomized"][dist] = []

    for size in sizes:
        arr = generate_test_data(size, dist)
        k = size // 2  # Find the median

        _, time_det = measure_time(median_of_medians, arr, k)
        _, time_rand = measure_time(quickselect, arr, k)

        results["Deterministic"][dist].append(time_det)
        results["Randomized"][dist].append(time_rand)

for dist in distributions:
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, results["Deterministic"][dist], marker='o', linestyle='-', label="Deterministic Selection (Median of Medians)")
    plt.plot(sizes, results["Randomized"][dist], marker='s', linestyle='-', label="Randomized Quickselect")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.title(f"Runtime Comparison on {dist.capitalize()} Data")
    plt.grid()
    
    # Save the plot instead of displaying it
    plt.savefig(f"runtime_comparison_{dist}.png")