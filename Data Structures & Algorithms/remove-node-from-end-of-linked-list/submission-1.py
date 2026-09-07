# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0

        curr = head

        while curr:
            length += 1
            curr = curr.next

        position = length - n

        pointer = 0

        prev, curr = None, head

        if position == 0:
            return head.next

        while pointer < position:

            prev = curr
            curr = curr.next
            pointer += 1
        
        prev.next = curr.next

        return head
    




        