# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    This function takes two linked lists, which represent numbers with number of digits equal to the length of the linked list,
    and adds them together. A linked list [3]->[0]->[2] represents the number 203, while [2]->[9] represents 92.
    
    The return type is the head of a linked list whose nodes represent the sum of the two numbers.
    
    type l1: ListNode
    type l2: ListNode
    rtype: ListNode
    """
    num1 = 0
    num2 = 0
    cur1 = l1
    cur2 = l2
    con1 = 1
    con2 = 1
    while cur1:
        num1 += con1 * cur1.val
        cur1 = cur1.next
        con1 *= 10
    while cur2:
        num2 += con2 * cur2.val
        cur2 = cur2.next
        con2 *= 10
    s = str(num1 + num2)
    ret = ListNode(int(s[-1]))
    s = s[:-1]
    cur = ret
    while s != '':
        cur.next = ListNode(int(s[-1]))
        s = s[:-1]
        cur = cur.next
    return ret
    
'''
#test.    
lis1 = ListNode(1)
lis1.next = ListNode(8)
lis1.next.next = ListNode(2)
lis2 = ListNode(3)
lis2.next = ListNode(9)
lis2.next.next = ListNode(4)
print(addTwoNumbers(lis1,lis2))
'''
