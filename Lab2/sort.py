def insertion_sort(array: list):
    for index in range(1, len(array)):
        key = array[index]
        j = index - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


def merge_sort(array: list):
    pass
