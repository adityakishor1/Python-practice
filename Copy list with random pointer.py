class Solution(object):
    def copyRandomList(self, head):
        if not head: return head
        
        clones = {}
        
        curr = head
        while curr:
            clones[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next: clones[curr].next = clones[curr.next]
            if curr.random: clones[curr].random = clones[curr.random]
            curr = curr.next
        
        return clones[head]
