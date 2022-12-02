class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                ls = haystack[i:i+len(needle)]
                if ls == needle:
                    return i
        return -1
