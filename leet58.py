class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        s = lst[-1]
        return len(s)
    
test = Solution
print(test.lengthOfLastWord(1, "luffy is still joyboy"))