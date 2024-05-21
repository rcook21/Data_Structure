'''
Ryan Cook
CSC 2720
Lab: Friday
Date: Jan 28
'''
def CountingSort(arr):
    top = max(arr)
 
    count_array = [0] * (top + 1)
 
    for n in arr:
        count_array[n] += 1
 
    for i in range(1, top + 1):
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(arr)
 
    for i in range(len(arr) - 1, -1, -1):
        output_array[count_array[arr[i]] - 1] = arr[i]
        count_array[arr[i]] -= 1
 
    return output_array

arr1 = [50, 11, 33, 21, 40, 50, 40, 40, 21]
arr2 = [17, 5, 41, 26, 21, 13, 8, 22]
arr3 = [22, 22, 22, 11, 6, 32, 18, 9]

print(CountingSort(arr1))
print(CountingSort(arr2))
print(CountingSort(arr3))