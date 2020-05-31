# Given a array, where each nested array stores the name and the grade, find the person with the second lowest grade. If the are more than one student with the same score sort them in alphabetical order.
python_students = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.2],
    ["Akriti", 41],
    ["Harsh", 39],
]


def sort_by_score(arr):
    end_index = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, end_index):
            if arr[i][1] > arr[i + 1][1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def second_lowest(arr):
    arr = sort_by_score(arr)
    second = arr[1][1]
    return [elem[0] for elem in arr if elem[1] == second]


def sort_by_letter(arr):
    arr = second_lowest(arr)
    print(arr)
    end_index = len(arr) - 1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, end_index):
            for j in range(0, len(arr) - 1):
                if alphabet.index(arr[i][j].lower()) > alphabet.index(
                    arr[i + 1][j].lower()
                ):
                    sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


print(sort_by_letter(python_students))
