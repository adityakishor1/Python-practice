class Solution(object):
    def decodeString(self, s):
        opt = ''
        k = ''
        stack = []

        for i, c in enumerate(s):
            if c=='[':
                stack.append(i)
            elif c==']':
                i_start = stack.pop()
                if not stack:
                    opt += int(k)*self.decodeString(s[i_start+1:i])
                    k = ''
            elif c.isdigit() and not stack:
                k+=c
            elif not stack:
                opt+=c
        return opt or s
