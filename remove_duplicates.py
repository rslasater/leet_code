class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        # nums is already sorted
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        # elements nums[:write] are unique
        return write

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
k = s.removeDuplicates(nums)
print(k, nums[:k])
