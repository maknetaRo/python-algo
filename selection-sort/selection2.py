def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


print(selection_sort([3, 5, 1, 6, 3, 7, 8, 0, 9]))
