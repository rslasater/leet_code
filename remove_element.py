nums = [1,2,2,4,5,1]
value_to_remove = 2
b = list(filter(lambda x: x!= value_to_remove, nums))
len(nums)-len(b)

class Solution(object):
    def removeElement(self, nums, val):
        pos = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1
        return pos

s = Solution()
s.removeElement([1,2,2,4], 2)
