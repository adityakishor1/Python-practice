class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def find_ancestors(target):
            ancestors = []
            curr = root
            while curr:
                ancestors.append(curr)

                if curr is target: break

                if target.val>curr.val:
                    curr = curr.right
                else:
                    curr = curr.left

            ancestors.reverse()
            return ancestors

        def find_lowest_common(a1, a2):
            if len(a1)>len(a2):
                a2 = set(a2)
                for node in a1:
                    if node in a2:
                        return node
            else:
                a1 = set(a1)
                for node in a2:
                    if node in a1:
                        return node
        
        p_ancestors = find_ancestors(p)
        q_ancestors = find_ancestors(q)
        return find_lowest_common(p_ancestors, q_ancestors)
