def insertion_sort(array: list):
    for index in range(1, len(array)):
        key = array[index]
        j = index - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


def merge(array: list, start: int, mid: int, end: int):
    left_array = array[start:mid]
    right_array = array[mid:end]

    left_index = 0
    right_index = 0
    array_index = start

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            array[array_index] = left_array[left_index]
            left_index = left_index + 1
        else:
            array[array_index] = right_array[right_index]
            right_index = right_index + 1
        array_index = array_index + 1

    while left_index < len(left_array):
        array[array_index] = left_array[left_index]
        left_index = left_index + 1
        array_index = array_index + 1
    while right_index < len(right_array):
        array[array_index] = right_array[right_index]
        right_index = right_index + 1
        array_index = array_index + 1


def merge_sort(array: list, start: int, end: int):
    if start >= end:
        return array
    mid = (start + end) // 2
    merge_sort(array, start, mid)
    merge_sort(array, mid + 1, end)
    merge(array, start, mid, end)
    return array
