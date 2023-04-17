import timeit

setup_code = """
from sort import insertion_sort, merge_sort
from random import sample
SIZE = 20_000
random_data = sample(range(0, SIZE), SIZE)
"""

is_code = """insertion_sort(random_data)"""
is_time = timeit.timeit(stmt=is_code, setup=setup_code, number=3)
print(f"Time taken by insertion sort: {is_time/3}")


ms_code = """merge_sort(random_data)"""
bs_time = timeit.timeit(stmt=ms_code, setup=setup_code, number=3)
print(f"Time taken by merge sort: {bs_time/3}")
