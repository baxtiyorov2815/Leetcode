class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mx = 0
        lst = []

        for i in nums:
            if i in lst:
                continue
            elif nums.count(i) > mx:
                mx = nums.count(i)
                s = i
                lst.append(i)

        return s