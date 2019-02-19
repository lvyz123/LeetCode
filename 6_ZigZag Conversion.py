class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        y_coor=0;letter=0
        record=[[] for i in range(numRows)]
        total_str='';down_flag=True
        while letter<len(s):
            record[y_coor].append(s[letter])
            if y_coor==numRows-1:
                down_flag=False
            elif y_coor==0:
                down_flag=True
            if down_flag==True and numRows>1:
                y_coor+=1
            elif down_flag==False and numRows>1:
                y_coor-=1
            letter+=1
        for j in range(numRows):
            str_sum=''.join(record[j])
            total_str+=str_sum
        return total_str
