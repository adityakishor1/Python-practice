class Solution(object):
    def lowestCommonAncestor(self, p, q):
        ancestorP = set()
        ancestorQ = set()
        
        temp = p
        while temp:
            ancestorP.add(temp)
            temp = temp.parent
        
        temp = q
        while temp:
            ancestorQ.add(temp)
            temp = temp.parent
        
        commonAncestor = ancestorQ.intersection(ancestorP)
        temp = q
        while temp:
            if temp in commonAncestor: return temp 
            temp = temp.parent
        return None
