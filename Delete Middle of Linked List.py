class Solution:
    def deleteMid(self,head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        if not head or not head.next:
            return None
        
        # Initialize two pointers slow and fast
        slow = fast = head
        prev = None
        
        # Traverse the list to find the middle node(s) using slow and fast pointers
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node(s)
        prev.next = slow.next
        
        return head
