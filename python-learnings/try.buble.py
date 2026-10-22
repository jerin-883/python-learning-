def buble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64,34,35,23,66,30,77,7,6,10]
print("original array:", arr)
buble(arr)
print("sorted array:",arr)