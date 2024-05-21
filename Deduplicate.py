'''
Ryan Cook
CSC 2720 Lab#2
Lab time: 1:00-1:50
Due time: 01/21 

'''
def deduplicate(input_lst):
    max_val = max(input_lst)
    count_lst = [0] * (max_val + 1)
    for num in input_lst:
        count_lst[num] += 1
    output_lst = [num for num in range(max_val + 1) if count_lst[num] > 0]
    return output_lst

print(deduplicate([50, 11, 33, 21, 40, 50, 40, 40, 21]))
print(deduplicate([1,1,1,1]))
print(deduplicate([18,4,10,1,7,11,4]))