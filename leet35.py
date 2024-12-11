class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        k = 0
        for i in nums:
            if i < target:
                k += 1

        return k