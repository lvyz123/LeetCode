class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol_set=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                l = 0
                r = len(nums) -1
                while l<r:
                    if l == i:
                        break
                    if r == j:
                        break
                    tmp = nums[i]+nums[j]+nums[l]+nums[r]
                    if tmp > target:
                        r -= 1
                    elif tmp < target:
                        l += 1
                    else:
                        sol_set.append([l,i,j,r])
        return sol_set
