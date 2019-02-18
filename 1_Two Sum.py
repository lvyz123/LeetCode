class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low_bd=0;high_bd=-1
        nums_init_rec=nums
        nums=sorted(nums)
        sum_num=nums[low_bd]+nums[high_bd]
        while sum_num!=target:
            if sum_num>target:
                high_bd-=1
            else:
                low_bd+=1
            sum_num=nums[low_bd]+nums[high_bd]
        index_low=nums_init_rec.index(nums[low_bd])
        nums_init_rec[index_low]='a'
        index_high=nums_init_rec.index(nums[high_bd])
        return index_low,index_high
