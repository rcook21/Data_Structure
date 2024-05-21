import random

n=int(input("Enter n: "))
while(n<=0):
    n=int(input("Enter a positive integer for n: "))
print("Welcome to Guess My Number!")
print("Please think of a number between 0 and %d"%(n-1))
low=0
high=n
while(True):
    num = random.randint(low,high)
    print("Is your number: %d?"%(num))
    print("Please enter C for correct, H for too high, or L for too low.")
    exit = 0
    while(True):
        guess = input("Enter your response(H/L/C): ")
        if(guess == "H"):
            high = num - 1
            break
        elif(guess == "L"):
            low = num + 1
            break
        elif(guess == "C"):
            exit = 1
            break
    if exit == 1:
        break
print("Thank you for playing Guess My Number!") 