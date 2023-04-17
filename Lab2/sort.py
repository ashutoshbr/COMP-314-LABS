def insertion_sort(array: list):
    for index in range(1, len(array)):
        key = array[index]
        j = index - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


def merge(left_array: list, right_array: list) -> list:
    sorted_array = [None] * (len(left_array) + len(right_array))
    left_index = right_index = array_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            sorted_array[array_index] = left_array[left_index]
            left_index = left_index + 1
        else:
            sorted_array[array_index] = right_array[right_index]
            right_index = right_index + 1
        array_index = array_index + 1

    while left_index < len(left_array):
        sorted_array[array_index] = left_array[left_index]
        left_index = left_index + 1
        array_index = array_index + 1
    while right_index < len(right_array):
        sorted_array[array_index] = right_array[right_index]
        right_index = right_index + 1
        array_index = array_index + 1

    return sorted_array


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)
