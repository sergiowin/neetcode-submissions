# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #remove the nth node away from the end of list
        #base cases
        if not head.next:
            return None
        
        # n is 1 indexed meaning the end is 1 etc
        cur = head
        leng = 1
        while cur.next:
            cur = cur.next
            leng += 1
        cur = head
        if leng == n:
            return head.next
        for i in range(leng - n - 1):
            cur = cur.next
        newNext = cur.next.next
        cur.next = newNext
        return head
        # fast is now at the end and slow is at the midpoint
        # first find out if n is in the first half or the second half
        