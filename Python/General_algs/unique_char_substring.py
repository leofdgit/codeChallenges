def lenLongestSubstring(strn):
    '''
    This function takes as input a string s and returns the longest substring whose characters are unique.
    
    The maximum length of such a substring is equal to the number of characters in the alphabet used to construct the string.
    If only lower case numbers are considered then the maximum length is 26, whereas a string containing upper and lower case
    characters could contain a unique substring of length 52.
    '''
    if len(strn) == 0:
        return 0
    largest_len = 0
    counter = 0
    dic = {}
    for i in strn:
        if i in dic:
            if counter > largest_len:
                largest_len = counter
            counter = 0
            dic = {}
        counter += 1
        dic[i] = 1
    largest_len = max(counter, largest_len)
    return largest_len
'''
#Test.
print(lenLongestSubstring('abcdabcdabcdeabcd'))
print(lenLongestSubstring('abABab'))
'''
