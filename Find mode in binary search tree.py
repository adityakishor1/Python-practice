class Solution(object):
    def findMode(self, root):
        if not root: return []
        
        ans = []
        stack = []
        prev_val = None
        curr = root
        curr_count = 0
        max_count = float('-inf')
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            
            #[0]
            if curr.val!=prev_val:
                curr_count = 1
                prev_val = curr.val
            else:
                curr_count += 1
            
            #[1]
            if curr_count>max_count:
                ans = [curr.val]
                max_count = curr_count
            elif curr_count==max_count:
                ans.append(curr.val)
            
            curr = curr.right
                
        return ans
