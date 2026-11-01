# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None: 
        carry = 0

        dummy = ListNode(0)
        current = dummy

        p1 = l1
        p2 = l2

        while(p1 !=None or p2 != None or carry !=0 ):
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            total = v1+v2+carry 
            digit = total % 10
            carry = total // 10
            new_node = ListNode(digit)
            current.next = new_node
            current = current.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        return dummy.next
            




        



        
        
        