class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        for i in digits:
            s += str(i)
        
        s = int(s)
        s += 1
        s = str(s)
        lst = []
        for i in range(len(s)):
            lst.append(int(s[i]))

        return lst