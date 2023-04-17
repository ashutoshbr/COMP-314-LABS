import matplotlib.pyplot as plt
from timeit import default_timer
from sort import insertion_sort, merge_sort
from random import sample

SIZE = 10_000
data_size = []
insertion_sort_time = []
merge_sort_time = []

for i in range(1, SIZE, 500):
    random_data = sample(range(0, SIZE), i)
    data_size.append(i)

    # Insertion Sort
    start_time = default_timer()
    insertion_sort(random_data)
    insertion_sort_time.append(default_timer() - start_time)

    # Merge Sort
    start_time = default_timer()
    merge_sort(random_data)
    merge_sort_time.append(default_timer() - start_time)


plt.plot(data_size, insertion_sort_time, label="Insertion Sort")
plt.plot(data_size, merge_sort_time, label="Merge Sort")
plt.legend()
plt.show()
