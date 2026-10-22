num = [1, 5, 4, 8, 2, 0, 9, 10]

largest = float('-inf')
second_largest = float('-inf')

for i in range(len(num)):
    if num[i] > largest:
        second_largest = largest
        largest = num[i]

    elif num[i] > second_largest and num[i] < largest:
        second_largest = num[i]

print("Second largest:", second_largest)