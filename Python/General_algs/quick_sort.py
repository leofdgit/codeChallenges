def quick_sort(l):
    quick_sort_help(l,0,len(l)-1)
    return l

def quick_sort_help(l,start,end):
    if start < end:
        pivot_point = partition(l,start,end)

        quick_sort_help(l,start,pivot_point-1)
        quick_sort_help(l,pivot_point+1,end)

def partition(l,start,end):
    pivot_value = l[start]
    left_count = start+1
    right_count = end
    done = False

    while not done:
        while (left_count <= right_count and l[left_count] <= pivot_value):
            left_count += 1
        while (left_count <= right_count and l[right_count] >= pivot_value):
            right_count -= 1
        if right_count < left_count:
            done = True
        else:
            temp = l[left_count]
            l[left_count] = l[right_count]
            l[right_count] = temp

    temp = l[start]
    l[start] = l[right_count]
    l[right_count] = temp
    return right_count


'''
#test
print(quick_sort([9,8,7,5,4,2,1]))
'''
