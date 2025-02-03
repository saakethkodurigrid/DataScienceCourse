#https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: ListNode) -> ListNode: # type: ignore
        prev = None  
        curr = head  

        while curr is not None:
            next_node = curr.next
            
            curr.next = prev  
            prev = curr  
            curr = next_node 
        return prev