class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums=sorted(nums)
        comb_rec=[]
        for i in range(len(nums)-2):
            j=i+1;k=len(nums)-1
            sum_three=sorted_nums[i]+sorted_nums[j]+sorted_nums[k]
            while j<k:
                if sum_three>0:
                    k-=1
                elif sum_three<0:
                    j+=1
                else:
                    comb=[sorted_nums[i],sorted_nums[j],sorted_nums[k]]
                    if comb not in comb_rec:
                        comb_rec.append(comb)
                    j+=1;k-=1
                sum_three=sorted_nums[i]+sorted_nums[j]+sorted_nums[k]
        return comb_rec
