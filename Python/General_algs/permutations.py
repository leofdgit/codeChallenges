def permutations(array):
    '''
    This function is a generator for all permutations of an array containing UNIQUE elements.
    
    A generator was chosen as the number of permutations is n! for an array of length n, which can be time consuming to 
    compute all at once. 
    
    To adjust for all unique permutations for an array potentially containing duplicates, one can instead write a regular 
    (read: non-generator) function that utilises a set to discard unwanted duplicates.
    '''
    if len(array) <= 1:
        yield array
    else: #take out an element and place in front of all permutations of remaining elements
        for i in range(len(array)):
            take_out = array[i]
            remainder = array[:i] + array[i+1:]
            for perm in permutations(remainder):
                yield [take_out] + perm
                
'''
Test.
print(permutations([1,2,3,4,5,6,7])
'''
