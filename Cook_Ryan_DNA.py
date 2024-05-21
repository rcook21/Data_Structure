'''
Ryan Cook
CSC 2720
Due Date: 04/09/24
'''
def RepeatedDnaSequences(s):
    identify, repeated = set(), set()
    for i in range(len(s) - 9):
        sequence = s[i:i + 10]
        if sequence in identify:
            repeated.add(sequence)
        identify.add(sequence)
    return list(repeated)

#Test Cases
print(RepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(RepeatedDnaSequences("AAAAAAAAAAAAA"))
print(RepeatedDnaSequences("ACACACACACAC"))