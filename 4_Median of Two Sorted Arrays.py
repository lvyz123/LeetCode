class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num_list=sorted(nums1+nums2)
        if len(num_list)%2==1:
            median=num_list[len(num_list)//2]
        else:
            median=(num_list[len(num_list)//2-1]+num_list[len(num_list)//2])/2
        return median
