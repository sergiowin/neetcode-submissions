# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prevNode = None
        targetNode = head
        nextNode = None
        while (targetNode != None):
            ## save next node to be edited
            nextNode = targetNode.next
            ## set the target to the previous node for reversal
            targetNode.next = prevNode
            ## set prevNode
            prevNode = targetNode
            ## move target node to the previous next node for next loop
            targetNode = nextNode
        
        return prevNode