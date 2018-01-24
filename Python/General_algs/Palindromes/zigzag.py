def zigzag(s,n):
    '''
    Takes as input a string s and an integer n and returns a string created by appending the characters in s to an empty string.
    The order in which they are appended is as follows: take characters n steps apart, starting from s[0]. When the end of the string
    is reached, repeat starting at s[1], then s[2],..., s[n-1].
    
    E.g. zigzag('abcabcabc',3) -> 'aaabbbccc'.
    '''
    ret = [[] for i in range(n)]
    for i in range(len(s)):
        indx = i % n
        ret[indx].append(s[i])
    ret =  [item for sublist in ret for item in sublist]
    rets = ''
    for r in ret:
        rets += r
    return rets
    
'''
#test
print(zigzag('aaabbbccc',3))
'''
