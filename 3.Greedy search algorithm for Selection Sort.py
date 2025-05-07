def greedy_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first unsorted element
        min_index = i

        # Find the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted one
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print current step
        print(f"Step {i + 1}: {arr}")

# Take user input
input_str = input("Enter numbers separated by spaces: ")
input_list = [int(x) for x in input_str.strip().split()]

print("\nSorting process:")
greedy_selection_sort(input_list)

print("\nSorted list:", input_list)
