import timeit

setup_code = """
from search import linear_search, binary_search
size = 1_000_000
big_data = list(range(size))

to_find = size + 1
"""

ls_code = """linear_search(to_find, big_data)"""
ls_time = timeit.timeit(stmt=ls_code, setup=setup_code, number=1)
print("Time taken by linear search for 100,000,000 data size: ", ls_time)


bs_code = """binary_search(to_find, big_data)"""
bs_time = timeit.timeit(stmt=bs_code, setup=setup_code, number=1)
print("Time taken by binary search for 100,000,000 data size: ", bs_time)
