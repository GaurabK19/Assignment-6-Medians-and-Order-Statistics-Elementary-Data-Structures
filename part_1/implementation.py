import random

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


# Example Usage
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 4], 2),  # Find 3rd smallest element (should return 3)
        ([10, 20, 30, 40, 50, 60, 70], 5),  # Find 6th smallest (should return 60)
        ([7, 7, 7, 7, 7, 7, 7], 3),  # All duplicates (should return 7)
        ([100], 0),  # Single element array (should return 100)
    ]

    for arr, k in test_cases:
        print(f"Array: {arr}, k: {k}")
        print(f"Deterministic Selection: {median_of_medians(arr, k)}")
        print(f"Randomized Quickselect: {quickselect(arr, k)}")
        print("-" * 40)