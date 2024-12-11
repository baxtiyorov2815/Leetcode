class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for i in nums:
            while nums.count(i) != 1:
                nums.remove(i)
                k += 1
        
        return len(nums)
    
