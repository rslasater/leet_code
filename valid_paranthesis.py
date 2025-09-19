class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in mapping.values():   # opening bracket
                stack.append(char)
            elif char in mapping:          # closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # ignore invalid characters or return False
                return False  

        return not stack         

s="({[}])"
sol = Solution()
sol.isValid(s)

