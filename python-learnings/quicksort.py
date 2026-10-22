def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        last = arr[-1]
        left = [x for x in arr[:-1] if x <= last]
        right = [x for x in arr[:-1] if x > last]

        return quick_sort(left) + [last] + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
