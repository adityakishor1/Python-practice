class Solution(object):
    def findKthLargest(self, nums, K):
        def quickSelect(A, s, e, K):
            pivot = A[(s+e)/2]
            i = s
            t = s
            j = e
            
            while t<=j:
                if A[t]<pivot:
                    A[i], A[t] = A[t], A[i]
                    i += 1
                    t += 1
                elif A[t]==pivot:
                    t += 1
                else:
                    A[t], A[j] = A[j], A[t]
                    j -= 1
            
            if e-j>=K:
                return quickSelect(A, j+1, e, K)
            elif e-i+1>=K:
                return pivot
            else:
                return quickSelect(A, s, i-1, K-(e-(i-1)))
            
        return quickSelect(nums, 0, len(nums)-1, K)
