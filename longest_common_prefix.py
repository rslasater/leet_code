class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        import os
        sol = os.path.commonprefix(strs)
        return sol

strs = ["flower","flow","flight"]

s = Solution()
s.longestCommonPrefix(strs)
