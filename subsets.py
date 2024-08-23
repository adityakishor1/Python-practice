class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        answer = [[]]
        for num in nums:
            new_subs = []
            for sub in answer:
                new_subs.append(sub+[num])
            answer.extend(new_subs)
        return list(set([tuple(combination) for combination in answer]))
