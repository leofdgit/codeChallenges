def mergeSort(l):
    '''
    Merge sort implementation. Note that if len(l) == 1, then l is returned (1-element list).
    If not, the left and right halves of l are sorted (read: split down into lists of length two, then build up
    to original list).
    
    '''
    if len(l) > 1:
        mid = len(l)//2
        leftHalf = l[:mid]
        rightHalf = l[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while (i < len(leftHalf) and j < len(rightHalf)):
            if leftHalf[i] < rightHalf[j]:
                l[k] = leftHalf[i]
                i += 1
            else:
                l[k] = rightHalf[j]
                j +=1
            k += 1
        while i < len(leftHalf):
            l[k] = leftHalf[i]
            i += 1
            k += 1
        while j < len(rightHalf):
            l[k] = rightHalf[j]
            j += 1
            k += 1
    return l
'''
#test
alist = [9,8,7,6,5,4,3,2,1]
mergeSort(alist)
print(alist)
alist = [9999999999999999,1,2,3,5438549357493854398]
mergeSort(alist)
print(alist)
'''
