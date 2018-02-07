def palnum(n):
     '''
     Returns True if the given number is a palindrome (False otherwise).
     This function does not use string methods.
     '''
    temp=n
    reverse=0
    while(n>0):
        dig = n % 10
        rev = reverse*10 + dig
        n = n // 10
    if(temp==reverse):
        return True
    else:
        return False
        
        
'''
#test
print(palnum(9998999))
print(palnum(12345678910))
'''
