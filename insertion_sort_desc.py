def insertion_sort_decreasing(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def run_tests():
    """
    Test the insertion sort with multiple test cases.
    """
    print("=" * 50)
    print("INSERTION SORT - DECREASING ORDER TESTS")
    print("=" * 50)
    
    test1 = [8, 3, 5, 2, 9, 1]
    print(f"\nTest 1 - Random array:")
    print(f"  Before: {test1}")
    insertion_sort_decreasing(test1)
    print(f"  After:  {test1}")
    
    test2 = [1, 2, 3, 4, 5]
    print(f"\nTest 2 - Already ascending:")
    print(f"  Before: {test2}")
    insertion_sort_decreasing(test2)
    print(f"  After:  {test2}")
    
    test3 = [10, 8, 6, 4, 2]
    print(f"\nTest 3 - Already descending:")
    print(f"  Before: {test3}")
    insertion_sort_decreasing(test3)
    print(f"  After:  {test3}")
    
    test4 = [5, 2, 8, 2, 9, 5]
    print(f"\nTest 4 - With duplicates:")
    print(f"  Before: {test4}")
    insertion_sort_decreasing(test4)
    print(f"  After:  {test4}")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    run_tests()