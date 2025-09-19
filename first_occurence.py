class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

haystack = 'leetcode'
needle = 'leeo'
s = Solution()
s.strStr(haystack, needle)
