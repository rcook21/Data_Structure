#Reverse list function 
'''
Ryan Cook
CSC 2720
Lab Fri 1:00-1:50
Due Date: 2/20/24
'''
def reverse(num):
    left = 0
    right = len(num) - 1
    
    while left < right:#while function to reverse
        num[left], num[right] = num[right], num[left]#flips right to left
        left += 1
        right -= 1
    
    return num

#Test Cases
num1 = [3, 4, 7, 6, 1]
num2 = [1,2,3,4,5,6,7,8]
num3 = [11,90,54,23,72,6,49]

reversed_num1 = reverse(num1)
print(reversed_num1)  
reversed_num2 = reverse(num2)
print(reversed_num2)
reversed_num3 = reverse(num3)
print(reversed_num3)


#end of program 