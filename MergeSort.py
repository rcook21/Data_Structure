'''
Ryan Cook
CSC 2720
Lab: Friday 1:00-1:50
2/11/24
'''

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2#Find middle and split array in half
        low = arr[:mid]
        high = arr[mid:]
        mergeSort(low)
        mergeSort(high)
        i = j = k = 0 #Sets everything equal

        #Merges the two halves back together
        while i < len(low) and j < len(high):
            if low[i] < high[j]:
                arr[k] = low[i]
                i += 1
            else:
                arr[k] = high[j]
                j += 1
            k += 1
        
        while i < len(low):
            arr[k] = low[i]
            i += 1
            k += 1

        while j < len(high):
            arr[k] = high[j]
            j += 1
            k += 1

#Deduplication Function
def deDuplication(arr): 
    mergeSort(arr)

    if  len(arr) <= 1:
        return arr
    
    #Finds unique elements in list
    index= 0
    for i in range(1, len(arr)):
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]

    #Deletes duplicate elements
    del arr[index + 1:]

if __name__ == "__main__":
    #Test Cases
    lst1 = [50, 11, 33, 21, 40, 50, 40, 40, 21]
    lst2 = [15, 27, 4, 39, 21, 19, 45, 32, 4, 4]
    lst3 = [1,1,1,1,1,1,1,1,33,22]
    deDuplication(lst1)
    deDuplication(lst2)
    deDuplication(lst3)

    print('Deduplicated Array:', lst1)
    print('Deduplicated Array:', lst2)
    print('Deduplicated Array:', lst3)
