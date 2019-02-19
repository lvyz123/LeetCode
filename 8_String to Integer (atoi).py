class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        if str=='' or ((str[0] not in ['+','-']) and str[0].isdigit()==False) or ((str[0] in ['+','-']) and (len(str)==1 or str[1].isdigit()==False)):
            return 0
        actual_num_str=''
        i=1 if str[0] in ['+','-'] else 0
        while i<len(str) and str[i].isdigit():
            actual_num_str+=str[i]
            i+=1
        if str[0]=='-':
            actual_num=-int(actual_num_str)
        else:
            actual_num=int(actual_num_str)
        if actual_num>2**31-1:
            actual_num=int(2**31-1)
        elif actual_num<-2**31:
            actual_num=int(-2**31)
        return actual_num
