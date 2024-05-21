def hasBalancedParentheses(s: str) -> bool:
    stack = []#Empty list
    # Dictionary for characters 
    mapping = {')': '(', '}': '{', ']': '['}#
    
    for char in s:#For loop
        if char in mapping.values():
            stack.append(char)#Checks mapping of char
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
    
    # If empty stack, all parentheses are balanced
    return not stack

# Output 

#Balanced parentheses test cases
print(hasBalancedParentheses("()"))  # True
print(hasBalancedParentheses("([{}])()"))  # True
print(hasBalancedParentheses(" "))  # True 

# Unbalanced parentheses test cases
print(hasBalancedParentheses("([)"))  # False
print(hasBalancedParentheses("(({}()}))"))  # False