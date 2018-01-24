def palindrome(s):
    '''
    Return True/False if string s is/isn't a palindrome.
    '''
    S = len(s)
    if S % 2 == 1:
        s = s[:S//2] + s[(S//2) + 1:]
    for i in range(int(len(s)/2)):
        if s[i] != s[-1-i]:
            return False
    return True
    
'''
#test
print(palindrome('abcba'))
print(palindrome('abaa'))
'''
   
