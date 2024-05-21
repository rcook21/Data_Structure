'''
Ryan Cook
CSC 2720
Lab Fri 1:00-1:50
Due Date: 2/20/24
'''
#Sort Flower Function
def sort_flowers(n, flowers):
     
    for i in range(1, n):#Insertion Sort
        key = flowers [i]
        j = i - 1 
        while j >= 0 and flowers [j] > key:#While loop to sort first letter
            flowers [j+1] = flowers [j]
            j -= 1
        flowers[j+1] = key
    return flowers 
#Test Cases
n = 3 
flower1 = ["Rose", "Lily", "Tulip"]
n = 3 
flower2 = ["Orchid", "Cherry Blossom", "Sunflower"]
n = 3 
flower3 = ["Hydrangea", "Daisy", "Chrysanthemum"]

print (sort_flowers(n, flower1))
print (sort_flowers(n, flower2))
print (sort_flowers(n, flower3))