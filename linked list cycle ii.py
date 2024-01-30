class Solution(object):
    def detectCycle(self, head):
        visited = set()
        curr = head
        while curr:
            if curr in visited: return curr
            visited.add(curr)
            curr = curr.next
        return None
