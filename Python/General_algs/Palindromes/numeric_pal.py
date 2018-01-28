def palnum(n):
     '''
     Returns True if the given number is a palindrome (False otherwise).
     This function does not use string methods.
     '''
    temp=n
    rev=0
    while(n>0):
        print(n)
        print(rev)
        dig = n % 10
        rev = rev*10 + dig
        n = n // 10
    if(temp==rev):
        return True
    else:
        return False
        
        
'''
#test
print(palnum(9998999))
print(palnum(12345678910))
'''
