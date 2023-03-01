def minimalHeaviestSetA(arr):
    # Write your code here
    arr.sort()
    summ = 0
    subSum = 0
    subArray = []
    j = 0
    
    for i in range(len(arr)):
        summ += arr[i]
    while subSum < summ:
        subArray[j] = arr.pop()
        subSum += subArray[j]
        j += 1

    print(subArray)
    return subArray.sort()