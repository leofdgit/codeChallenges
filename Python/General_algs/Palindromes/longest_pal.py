'''
Two functions to compute the longest palindromic substring in an input string s.

The first, longestPal, considers all substrings (from longest to shortest), and thus has run time of n! in the worst case.

The second, lonPal, expands around each character in the string (and the in-between of two characters). Expanding starts
with a single character (or no characters, if in between two characters) and looks at the characters on either side. If the
two characters on either side of the character are the same, the two characters are appended to either side of the original
character and the process is repeated for the resulting string (now of length 2/3).

The complexity of the second is thus n^2, as we consider 2n-1 centres, each iteration having a run time of order n.
'''


def longestPal(s):
    S = len(s)
    counter = S
    if palindrome(s):
        return s
    while counter != 0:
        counter -= 1
        for i in range(S - counter+1):
            if palindrome(s[i:i+counter]):
                return s[i:i+counter]
    return s[0]


def lonPal(s):
    start = end = 0
    for i in range(len(s)-1):
        len1 = expandAroundCenter(s,i,i)
        len2 = expandAroundCenter(s,i,i+1)
        lenm = max(len1,len2)
        if (lenm > end - start):
            start = i - (lenm - 1) / 2
            end = i + lenm / 2
    return s[int(start):int(end+1)]

def expandAroundCenter(s, l, r):
    L, R = l, r
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L-=1
        R+=1
    return R - L - 1
    
    
    
'''
#test
print(longestPal('fsdiuuhuufjoseijf'))
print(lonPal('fsdiuuhuufjoseijf'))
'''
