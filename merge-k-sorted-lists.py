class Solution(object):
    def mergeKLists(self, lists):
        h = [(node.val, node) for node in lists if node]
        heapq.heapify(h)
        
        preHead = ListNode()
        curr = preHead
        
        while h:
            _, node = heapq.heappop(h)
            if node.next: heapq.heappush(h, (node.next.val, node.next))
            curr.next = node
            curr = curr.next
        
        return preHead.next
