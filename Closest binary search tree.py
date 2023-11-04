class Solution(object):
    def closestValue(self, root, target):
        node = root
        ans = float('inf')
        
        while node:
            if not node: break
            
            if abs(ans-target)>abs(node.val-target):
                ans = node.val
            
            if target>node.val:
                node = node.right
            else:
                node = node.left
                
        return ans
