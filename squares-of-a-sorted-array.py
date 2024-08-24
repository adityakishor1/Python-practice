class Solution(object):
    def sortedSquares(self, numbers):
        if not numbers: return numbers

        if numbers[0]>=0:
            return [n**2 for n in numbers]

        m = 0
        for i, n in enumerate(numbers):
            if n>=0:
                m = i
                break

        A, B = numbers[m:], [-1*n for n in reversed(numbers[:m])]
        return [n**2 for n in self.merge(A, B)]

    def merge(self, A, B):
        a = b = 0
        opt = []
        while a<len(A) and b<len(B):
            if A[a]<B[b]:
                opt.append(A[a])
                a+=1
            else:
                opt.append(B[b])
                b+=1
        if a<len(A): opt.extend(A[a:])
        if b<len(B): opt.extend(B[b:])
        return opt
