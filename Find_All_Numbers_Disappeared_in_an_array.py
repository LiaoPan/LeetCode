class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        d = set(range(1,len(nums)+1))
        print list(d.difference(s))

t = Solution()
nums = [4,3,2,7,8,2,3,1]
t.findDisappearedNumbers(nums)


