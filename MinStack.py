'''
Ryan Cook
CSC 2720
Lab Time: Friday 1:00-1:50
Due Date: 3/10/24
'''

class MinStack:
    def __init__(self):#empty lists
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        #Pushes value onto stack
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        #Removes element on top of stack
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:

        #Gets the top element of stack 
        return self.stack[-1]

    def getMin(self) -> int:
        #Retrieves minimum element in stack.
        return self.min_stack[-1]
    

# MinStack object
min_stack = MinStack()

# Test push method
min_stack.push(5)
min_stack.push(3)
min_stack.push(8)
assert min_stack.stack == [5, 3, 8]
assert min_stack.min_stack == [5, 3]

# Test pop method
min_stack.pop()
assert min_stack.stack == [5, 3]
assert min_stack.min_stack == [5, 3]

# Test top method
assert min_stack.top() == 3
print(min_stack.top())

# Test getMin method
assert min_stack.getMin() == 3
print(min_stack.getMin())

min_stack.push(2)
assert min_stack.getMin() == 2
print(min_stack.push(2))

min_stack.push(10)
assert min_stack.getMin() == 2
print(min_stack.push(10))

print("Test Cases Passed!")
#end of program 