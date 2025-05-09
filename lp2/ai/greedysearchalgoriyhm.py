def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Main function
if __name__ == '__main__':
    arr = list(map(int, input("Enter the elements separated by space: ").split()))
    print("Original array:", arr)
    sorted_arr = selectionSort(arr)
    print("Sorted array:", sorted_arr)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
    def selectionSort(arr):
    # Get the length of the array
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Assume the current index as the minimum
        min_idx = i

        # Find the minimum element in the unsorted part of the array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Return the sorted array
    return arr

# Main function
if __name__ == '__main__':
    # Take input from the user, split by spaces and convert to integers
    arr = list(map(int, input("Enter the elements separated by space: ").split()))

    # Print the original array
    print("Original array:", arr)

    # Call the selectionSort function and store the sorted array
    sorted_arr = selectionSort(arr)

    # Print the sorted array
    print("Sorted array:", sorted_arr) '''
