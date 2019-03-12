class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_dis = 1e6
        res = 0
        for i in range(len(nums)):
            l = 0
            r = len(nums) -1
            while l<r:
                if l == i:
                    break
                if r == i:
                    break
                tmp = nums[i]+nums[l]+nums[r]
                if abs(tmp-target) < min_dis:
                    min_dis = abs(tmp-target)
                    res = tmp
                if tmp > target:
                    r -= 1
                elif tmp < target:
                    l += 1
                else:
                    return target
        return res
