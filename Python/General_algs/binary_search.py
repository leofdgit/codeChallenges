def binarySearch(array, item):
    '''
    Takes as input a sorted array of integers and an integer n, and outputs boolean expression (n in array).
    
    Recursive approach used to implement algorithm.
    '''
    a = len(array)
    if a == 0:
        return False
    if a == 1:
        return (item == array[0])
    mid = (a+1) //2
    midval = array[mid]
    if midval == item:
        return True
    p1, p2 = array[:mid], array[mid+1:]
    if item > midval:
        return binarySearch(p2,item)
    return binarySearch(p1,item)
    
'''
#test
print(binarySearch([1,3,5,11,33,57,99,100],99))
print(binarySearch([1,3,5,11,33,57,99,100],98))
'''
