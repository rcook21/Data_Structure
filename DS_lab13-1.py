"""
    Time Complexity: 
    O(nlogk) where n is the # of items in the list. The heap operations takes
    O(logk) time and the for loop runs n times for each item in list. 
    
    Space Complexity is O(k) to store heap of size k

 """
#built-in class for Heaps 
import heapq

def kBiggest(lst, k):

    if len(lst) < k:
        return None

    #heap w/ first k elements of lst
    min_heap = lst[:k]
    heapq.heapify(min_heap)

    #rest of the list
    for num in lst[k:]:
        # if larger than smallest, replace
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    # root represents kth largest element
    return min_heap[0]

if __name__ == "__main__":
    result = kBiggest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 2)
    result1 = kBiggest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 1)
    result2 = kBiggest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 5)
    print("The second largest number is:", result)
    print("The largest number is:", result1)
    print("The fifth largest number is:", result2)