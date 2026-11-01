# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def reverse(ll):
            prev = None
            current = ll
            while(current!= None):
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                
            return prev
        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0
        root = ListNode(0)

        current = root

        p1 = l1
        p2 = l2

        while(p1 or p2):
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            total = v1+v2+carry
            digit = total%10
            carry = total // 10
            new_node = ListNode(digit)
            current.next = new_node
            current = current.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        if carry:
            current.next = ListNode(carry)
        return reverse(root.next)

        