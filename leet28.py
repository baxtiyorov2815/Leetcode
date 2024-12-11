class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 1 and haystack[0] == needle:
            return 0
        for i in range(len(haystack)):
            for j in range(i, len(haystack)+1):
                print(i, j)
                print(haystack[i: j])
                if haystack[i: j] == needle:
                    return i
                
        return -1
    
test = Solution
print(test.strStr(1, "abc", "c"))