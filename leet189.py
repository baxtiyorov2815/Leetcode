class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        new_array = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if i + k > len(nums):
                print(1)
                new_array[i + k - 2] = nums[i]
            
            else:
                new_array[i + k - 1] = nums[i]

        nums = new_array
        print(nums)

test = Solution()
test.rotate(nums = [1,2,3,4,5,6,7], k = 3)