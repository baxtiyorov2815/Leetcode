class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1 += nums2
        k = nums1.count(0)
        lst = sorted(nums1)
        nums1 = lst[k:]
        
        return nums1

test = Solution()
test.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)