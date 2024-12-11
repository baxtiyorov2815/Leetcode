class Solution:
    def twoSum(self, nums, target: int):
        lst = []
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    lst.append(i)
                    lst.append(j)
                    break

        return lst
    
test1 = Solution()
print(test1.twoSum([3,2,4], 6))