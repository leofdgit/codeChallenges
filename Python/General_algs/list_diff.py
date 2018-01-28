def listDif(l1,l2):
    '''
    Returns the elements in l2 but not l1.
    '''
    container = {}
    for i in l1:
        container[i] = ['A']
    for j in l2:
        if j in container:
            container[j] = ['A','B']
        else:
            container[j] = ['B','B','B']
    ret = [k for k in container if len(container[k]) == 3]
    return ret



'''
#test
print(listSame([1,1,9,4,10000,32],[32,943249,25453])
print(listSame([1,1,9,4,10000,32],[943249,25453])
'''
