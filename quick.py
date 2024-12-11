import random
import time

def bubbleSort(arr):
    operation_count = 0
    n = len(arr)
    for x in range(n-1):
        swap = False
        for y in range(n-x-1):
            operation_count += 1
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
                operation_count += 1
                swap = True
        if swap == False:
            break
    return operation_count

# User input for the number of iterations
x = int(input("Enter the number of times to run the bubble sort: "))
total_operations = 0

for i in range(x):
    array = []
    for a in range(1, 100):
        randNum = random.randint(0, 100)
        array.append(randNum)

    operations = bubbleSort(array)
    total_operations += operations

average_operations = total_operations / x
print(f"[*] Average operations over {x} runs: {average_operations}")
