
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
#UPDATE (2016/2/13):
#The return format had been changed to zero-based indices. Please read the above updated description carefully.
#

nums = [3, 2, 4]
nums = [0, 4, 3, 0]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # init hash
        pool = {}
        i = 0
        while i < len(nums):
            k = '%d' % nums[i]
            if k in pool:
                pool[k].append(i)
            else:
                pool[k] = [i,]
            i += 1

        for k in pool.keys():
            n = '%d' % (target - int(k))
            if n in pool:
                for idx1 in pool[k]:
                    for idx2 in pool[n]:
                        if idx1 != idx2:
                            return [idx1, idx2]
        return []
    def twoSum_v1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                print('comp, %d, %d' % (i, j))
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j += 1
                    continue
            i += 1
        return []

s = Solution()
r = s.twoSum(nums, 0)
print(r)

