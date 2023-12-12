class Solution(object):
    def findMin(self, A):
        N = len(A)
        l = 0
        r = N-1
        
        while l<r:
            #skip the same
            while l<N-1 and A[l]==A[l+1]: l += 1
            while 0<r and A[r]==A[r-1]: r -= 1
            while l<N-1 and A[l]==A[r]: l += 1
            while 0<r and A[l]==A[r]: r -= 1
                
            m = (l+r)/2
            
            if A[l]<=A[m] and A[m]<=A[r]:
                #l~r is in-order, A[l] is the smallest.
                return A[l]
            elif A[l]<=A[m]:
                #l~m is in-order, m~r is rotated. smallet must be in m~r
                l = m+1
            else:
                #m~r is in-order, l~m is rotated. smallet must be in l~m
                r = m
        return A[l]
