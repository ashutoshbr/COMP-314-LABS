def linear_search(to_find: int, random_data: list) -> int | None:
    for index, elem in enumerate(random_data):
        if elem == to_find:
            return index

    return None


def binary_search(to_find: int, sorted_data: list) -> int | None:
    low = 0
    high = len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_data[mid] == to_find:
            return mid
        elif sorted_data[mid] < to_find:
            low = mid + 1
        elif sorted_data[mid] > to_find:
            high = mid - 1

    return None
