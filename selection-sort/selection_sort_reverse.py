def find_biggest_number(arr):
    biggest = arr[0]
    biggest_index = 0

    for i in range(1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        biggest = find_biggest_number(arr)
        new_arr.append(arr.pop(biggest))
    return new_arr


print(find_biggest_number([1, 4, 2, 6, 8, 9, 4, 5]))
print(selection_sort([1, 4, 2, 6, 8, 9, 4, 5]))
