class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        if k>len(nums1)*len(nums2): k = len(nums1)*len(nums2)
            
        ans = []
        h = [(nums1[0]+nums2[0], 0, 0)] #[0]
        seen = set([(0,0)]) #[2]
        
        while len(ans)<k: #[1]
            s, i, j = heapq.heappop(h)
            ans.append((nums1[i], nums2[j]))

            if i+1<len(nums1) and (i+1, j) not in seen:
                heapq.heappush(h, (nums1[i+1]+nums2[j], i+1, j))
                seen.add((i+1, j))

            if j+1<len(nums2) and (i, j+1) not in seen:
                heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))
                seen.add((i, j+1))
                
        return ans
