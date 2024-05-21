'''
Ryan Cook
CSC 2720
Lab Fri 1:00-1:50
Due Date: 2/20/24
'''
#Duplicate Finder
def dup_finder(n, words): 
    wset = set()
    for word in words: 
        if word in wset: #if function to find dups
            return True 
        wset.add(word)
    return False 

#Output 
if __name__== "__main__":
    lst1 = ["spring", "summer", "fall", "winter"] #False
    lst2 =  ["summer", "fall", "winter", "spring", "summer"] #True
    lst3 = ["computer", "data", "structure"] #False

    print(dup_finder(4, lst1))
    print(dup_finder(5, lst2))
    print(dup_finder(3, lst3))

