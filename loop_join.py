'''
Ryan Cook
CSC 2720
HW1
2/6/24
'''

def loop_join(lst1, lst2):
    result_list = [] #An empty list for the function to loop through

    
    m = len(lst1) #Variables to find the length of lst1 and lst2
    n = len(lst2) 
     
    i = 0  
    j = 0  

     
    while i < m and j < n:#Moves through the lists til i and j are equal to the length
         
        if lst1[i] == lst2[j]:#Adds to result_list if i and j are equal
            result_list.append(lst1[i])

            i += 1
            j += 1

            
            while i < m and lst1[i] == lst1[i - 1]:
                i += 1
            while j < n and lst2[j] == lst2[j - 1]:
                j += 1
        elif lst1[i] < lst2[j]:#Continues through lst1 if i is less than j and vise versa
           
            i += 1
        else:
            
            j += 1

    return result_list  


array1 = [1, 5, 6, 6, 9, 9, 9, 11, 11, 21]
array2 = [6, 6, 9, 11, 21, 21, 21]

result = loop_join(array1, array2)

print(f"LST: {result}")#The print statement will output the joined array