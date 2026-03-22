import random
import time
import sys

# Optional: increase recursion limit for larger tests
sys.setrecursionlimit(100000)


# ---------------------------
# Randomized Quicksort
# ---------------------------
def randomized_quicksort(arr):
    a = arr.copy()
    _randomized_quicksort(a, 0, len(a) - 1)
    return a


def _randomized_quicksort(a, low, high):
    if low < high:
        pivot_index = randomized_partition(a, low, high)
        _randomized_quicksort(a, low, pivot_index - 1)
        _randomized_quicksort(a, pivot_index + 1, high)


def randomized_partition(a, low, high):
    random_index = random.randint(low, high)
    a[random_index], a[high] = a[high], a[random_index]
    return partition(a, low, high)


# ---------------------------
# Deterministic Quicksort
# Pivot = first element
# ---------------------------
def deterministic_quicksort(arr):
    a = arr.copy()
    _deterministic_quicksort(a, 0, len(a) - 1)
    return a


def _deterministic_quicksort(a, low, high):
    if low < high:
        pivot_index = deterministic_partition_first(a, low, high)
        _deterministic_quicksort(a, low, pivot_index - 1)
        _deterministic_quicksort(a, pivot_index + 1, high)


def deterministic_partition_first(a, low, high):
    # Move first element to end, then reuse Lomuto partition
    a[low], a[high] = a[high], a[low]
    return partition(a, low, high)


# ---------------------------
# Common partition function (Lomuto)
# ---------------------------
def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


# ---------------------------
# Input generators
# ---------------------------
def generate_random_array(n):
    return [random.randint(0, 100000) for _ in range(n)]


def generate_sorted_array(n):
    return list(range(n))


def generate_reverse_sorted_array(n):
    return list(range(n, 0, -1))


def generate_repeated_array(n):
    return [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]


# ---------------------------
# Timing utility
# ---------------------------
def measure_time(sort_function, arr):
    start = time.perf_counter()
    sort_function(arr)
    end = time.perf_counter()
    return end - start


# ---------------------------
# Experiment runner
# ---------------------------
def run_experiments():
    sizes = [100, 500, 1000, 2000, 5000]

    distributions = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reverse Sorted": generate_reverse_sorted_array,
        "Repeated Elements": generate_repeated_array
    }

    print(f"{'Size':<8} {'Distribution':<20} {'Randomized QS (s)':<20} {'Deterministic QS (s)':<22}")
    print("-" * 75)

    for size in sizes:
        for name, generator in distributions.items():
            arr = generator(size)

            rand_time = measure_time(randomized_quicksort, arr)
            det_time = measure_time(deterministic_quicksort, arr)

            print(f"{size:<8} {name:<20} {rand_time:<20.6f} {det_time:<22.6f}")


if __name__ == "__main__":
    run_experiments()