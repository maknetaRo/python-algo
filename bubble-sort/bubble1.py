def bubble_sort(arr):
    end_index = len(arr) - 1
    sorted = False
    counter = (
        0  # to count how many times it goes through the loop until sorts the array
    )

    while not sorted:
        sorted = True
        for i in range(0, end_index):
            if arr[i] > arr[i + 1]:
                # if first element is bigger than second, the sorted flag is False and the elements have to be swapped
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                counter += 1
    return f"Sorted array: {arr}, counter: {counter}"


print(bubble_sort([2, 1]))

print(bubble_sort([2, 1, 3]))

print(bubble_sort([2, 1, 3, 5, 8, 6, 9, 7, 4]))
