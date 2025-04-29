class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None

class Solution:
    def segregate(self, head):
        count = [0, 0, 0]
        curr = head
        while curr:
            count[curr.data] += 1
            curr = curr.next
        curr = head
        i = 0
        while curr:
            if count[i] == 0:
                i += 1
            else:
                curr.data = i
                count[i] -= 1
                curr = curr.next
                
        return head
