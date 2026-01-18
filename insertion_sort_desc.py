"""
MSCS532 Assignment 1: Insertion Sort Algorithm
Basic implementation - sorts in decreasing order
"""

def insertion_sort_decreasing(arr):
    """
    Sorts array in decreasing order using Insertion Sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


if __name__ == "__main__":
    data = [8, 3, 5, 2, 9, 1]
    print("Original array:", data)
    insertion_sort_decreasing(data)
    print("Sorted array:", data)