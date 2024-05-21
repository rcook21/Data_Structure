'''
Ryan Cook
CSC2720
Lab Time: Friday 1:00-1:50
Due Date: 03/03/24
'''

from collections import deque

class MaxQueue:
    def __init__(self):
        self.main_queue = deque() #store elements 
        self.max_queue = deque() #store max

    def enqueue(self, element):
        self.main_queue.append(element)

        while self.max_queue and element > self.max_queue[-1]:
            self.max_queue.pop()
        
        self.max_queue.append(element)

    def dequeue(self):
        if not self.main_queue:
            return None

        popped_element = self.main_queue.popleft()

        if popped_element == self.max_queue[0]:
            self.max_queue.popleft()

        return popped_element#return queue

    def max_value(self):
        if not self.max_queue:
            return None
        return self.max_queue[0]#Return max output

#Test Cases
max_queue = MaxQueue()
max_queue.enqueue(1)
max_queue.enqueue(4)
max_queue.enqueue(2)
max_queue.enqueue(3)


print(max_queue.max_value())  # Output: 4
print(max_queue.max_value())  # Output: 4

max_queue.dequeue()
max_queue.dequeue()

print(max_queue.max_value())  # Output: 3

max_queue.dequeue()
max_queue.dequeue()

print(max_queue.max_value())  # Output: None