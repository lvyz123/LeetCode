class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_num=str(x)
        if str_num[0]=='-':
            new_str_num=str_num[:0:-1]
            new_x=-int(new_str_num)
        else:
            new_str_num=str_num[::-1]
            new_x=int(new_str_num)
        if new_x>2**31-1 or new_x<-2**31:
            new_x=0
        return new_x
