import random

def rand_choice(s):
    '''
    Returns a random element from the set s. Each element is equally likely to be chosen.
    '''
    l = list(s)
    le = len(l)
    if le == 0:
        return -1
    i = random.uniform(0,1) * le
    i = int(round(i,0))
    return l[i]
'''
#test
s = set([3,6,2,7,1, 'a'])
print(rand_choice(s))
'''
