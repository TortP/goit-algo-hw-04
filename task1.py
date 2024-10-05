import random
import timeit

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Вбудований алгоритм сортування (Timsort)
def timsort(arr):
    return sorted(arr)

# Функція для заміру часу виконання алгоритмів
def measure_time(sort_function, data):
    return timeit.timeit(lambda: sort_function(data.copy()), number=1)

# Генерація тестових даних
data_sizes = [100, 1000, 5000, 10000]
merge_times = []
insertion_times = []
timsort_times = []

for size in data_sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    merge_times.append(measure_time(merge_sort, data))
    insertion_times.append(measure_time(insertion_sort, data))
    timsort_times.append(measure_time(timsort, data))

# Побудова графіків
print("\nПорівняння алгоритмів сортування (Час виконання в секундах):")
print("Розмір даних\tMerge Sort\tInsertion Sort\tTimsort")
for i, size in enumerate(data_sizes):
    print(f"{size}\t\t{merge_times[i]:.6f}\t{insertion_times[i]:.6f}\t{timsort_times[i]:.6f}")


# Реалізація функції merge_k_lists для об'єднання k відсортованих списків у один

def merge_k_lists(lists):
    if not lists:
        return []
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged_lists.append(merge_two_lists(lists[i], lists[i + 1]))
            else:
                merged_lists.append(lists[i])
        lists = merged_lists
    return lists[0]

def merge_two_lists(l1, l2):
    result = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result

# Тест додаткової функції
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("\nВідсортований список після об'єднання k відсортованих списків:")
print(merged_list)