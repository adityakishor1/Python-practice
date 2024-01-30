class Solution(object):
    def hasCycle(self, head):
        visited = set()
        curr = head
        while curr:
            if curr in visited: return True
            visited.add(curr)
            curr = curr.next
        return False
        
