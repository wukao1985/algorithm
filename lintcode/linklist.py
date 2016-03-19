from __future__ import print_function

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def formList(A):
    rhead = ListNode(0)
    rtail = rhead
    for i in A:
        rtail.next = ListNode(i)
        rtail = rtail.next
    return rhead.next

def printList(head):
    while head is not None:
        print(head.val, '->', end = '')
        head = head.next
    print('null')

def findMidNode(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head.next
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(head1, head2):
    if head1 is None and head2 is None:
        return None
    
    dummy = ListNode(0)
    cur  = dummy
    while head1 is not None and head2 is not None:           
        if  head1.val < head2.val:
            cur.next = head1
            head1    = head1.next
        else:
            cur.next = head2
            head2    = head2.next
        cur = cur.next
            
    if head1 is None:
        cur.next = head2
    else:
        cur.next = head1

    return dummy.next

def reverseList(head):
    if head is None or head.next is None:
        return head
    
    pre = None
    while head is not None:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    
    return pre

def findKth(head, k):
    for i in xrange(k):
        if head is None:
            return None
        head = head.next
    return head
