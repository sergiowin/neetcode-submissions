# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        # if head.next == None:
        #     exit
        # elif head.next.next == None:
        #     return head
        while fast.next != None:
            fast = fast.next
            if fast.next != None:
                slow = slow.next
                fast = fast.next
        head2 = slow.next 
        slow.next = None # remove the middles next since we dont want there to by cycles.

  
        prev = None
        cur = head2
        tmp = None
        while cur != None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        cur = head
        while prev != None:
            tmp = cur.next
            cur.next = prev
            prev = prev.next
            cur = cur.next
            cur.next = tmp
            cur = cur.next
        
            

        