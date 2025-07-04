class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1
