def right_rotate(arr, k):
    n = len(arr)
    k = k % n  
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
k = 2
rotated = right_rotate(arr, k)
print("Original:", arr)
print("Right Rotated:", rotated)
