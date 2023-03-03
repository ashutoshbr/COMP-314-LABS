import timeit

setup_code = """
from search import linear_search, binary_search
SIZE = 10_000_000
big_data = list(range(SIZE))

to_find = SIZE + 1
"""

ls_code = """linear_search(to_find, big_data)"""
ls_time = timeit.timeit(stmt=ls_code, setup=setup_code, number=10)
print(f"Time taken by linear search: {ls_time/10}")


bs_code = """binary_search(to_find, big_data)"""
bs_time = timeit.timeit(stmt=bs_code, setup=setup_code, number=10)
print(f"Time taken by binary search: {bs_time/10}")
