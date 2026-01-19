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
    Run comprehensive test cases for the insertion sort algorithm.
    """
    print("=" * 60)
    print("INSERTION SORT - MONOTONICALLY DECREASING ORDER")
    print("=" * 60)
    
    test1 = [8, 3, 5, 2, 9, 1]
    print(f"\nTest 1 - Random array:")
    print(f"  Before: {test1}")
    insertion_sort_decreasing(test1)
    print(f"  After:  {test1}")
    
    test2 = [1, 2, 3, 4, 5]
    print(f"\nTest 2 - Ascending (worst case):")
    print(f"  Before: {test2}")
    insertion_sort_decreasing(test2)
    print(f"  After:  {test2}")
    
    test3 = [10, 8, 6, 4, 2]
    print(f"\nTest 3 - Descending (best case):")
    print(f"  Before: {test3}")
    insertion_sort_decreasing(test3)
    print(f"  After:  {test3}")
    
    test4 = [5, 2, 8, 2, 9, 5]
    print(f"\nTest 4 - With duplicates:")
    print(f"  Before: {test4}")
    insertion_sort_decreasing(test4)
    print(f"  After:  {test4}")
    
    test5 = [42]
    print(f"\nTest 5 - Single element:")
    print(f"  Before: {test5}")
    insertion_sort_decreasing(test5)
    print(f"  After:  {test5}")
    
    test6 = []
    print(f"\nTest 6 - Empty array:")
    print(f"  Before: {test6}")
    insertion_sort_decreasing(test6)
    print(f"  After:  {test6}")
    
    test7 = [3, -1, 4, -5, 2, 0]
    print(f"\nTest 7 - Mixed positive/negative:")
    print(f"  Before: {test7}")
    insertion_sort_decreasing(test7)
    print(f"  After:  {test7}")
    
    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)


def interactive_mode():
    """
    Interactive mode - allows user to input custom array for sorting.
    """
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE")
    print("=" * 60)
    
    try:
        user_input = input("\nEnter numbers separated by spaces: ")
        user_array = [int(x) for x in user_input.split()]
        
        print(f"\nYour array: {user_array}")
        insertion_sort_decreasing(user_array)
        print(f"Sorted (decreasing): {user_array}")
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_tests()
    
    print("\n")
    choice = input("Would you like to try your own array? (y/n): ")
    if choice.lower() == 'y':
        interactive_mode()
    
    print("\nThank you for using Insertion Sort!")