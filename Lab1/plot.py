import matplotlib.pyplot as plt
from timeit import default_timer
from search import linear_search, binary_search

SIZE = 10_000_000
TO_SEARCH = SIZE + 1

ls_data_size = []
ls_time_taken = []
bs_data_size = []
bs_time_taken = []

# Linear Search
for i in range(1, SIZE, 500_000):
    ls_data_size.append(i)

    data_list = list(range(i))
    start_time = default_timer()
    linear_search(TO_SEARCH, data_list)
    ls_time_taken.append(default_timer() - start_time)

# Binary Search
for i in range(1, SIZE, 500_000):
    bs_data_size.append(i)

    data_list = list(range(i))
    start_time = default_timer()
    binary_search(TO_SEARCH, data_list)
    bs_time_taken.append(default_timer() - start_time)

plt.plot(ls_data_size, ls_time_taken, label="Linear Search")
plt.plot(bs_data_size, bs_time_taken, label="Binary Search")
plt.legend()
plt.show()
