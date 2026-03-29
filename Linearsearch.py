import time
import matplotlib.pyplot as plt
import random

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return the index where it's found
    return -1  # Return -1 if not found

n_values = [100, 1000, 5000, 10000, 20000, 50000]
time_values = []

for n in n_values:
    # Generate a list of size n
    arr = [random.randint(0, n) for _ in range(n)]
    x = -1  # We use -1 to force the worst-case scenario (searching the whole list)

    start_time = time.perf_counter() # More precise than time.time()
    linear_search(arr, x)
    end_time = time.perf_counter()

    time_values.append(end_time - start_time)

# Plotting the results
plt.plot(n_values, time_values, marker='o', linestyle='-', color='b')
plt.title("Linear Search Time Complexity")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True)
plt.show()