from typing import List 

def postfixExpression(tokens: List[str]) -> int:
    stack = []#empty list
    for token in tokens:#for loop
        if token.isdigit():
            stack.append(int(token))#puts token in loop
        else:
            number2 = stack.pop()
            number1 = stack.pop()
            if token == '+':#adds numbers
                stack.append(number1 + number2)

            elif token == '-':#subtracts numbers
                stack.append(number1 - number2)

            elif token == '*':#multiplies numbers
                stack.append(number1 * number2)

            elif token == '/':#divides numbers
                stack.append(number1 // number2)  
                
    return stack.pop()#returns stack

# Test cases
print(postfixExpression(["1", "2", "*", "5", "+"])) 
print(postfixExpression(["6", "9", "-", "4", "*"]))  
print(postfixExpression(["2", "3", "7", "/", "+"])) 