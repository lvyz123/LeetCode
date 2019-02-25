class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        symbol_list=['I','V','X','L','C','D','M']
        value_list=[1,5,10,50,100,500,1000]
        for index,letter in enumerate(s):
            pos=symbol_list.index(letter)
            if index<len(s)-1:
                pos_next=symbol_list.index(s[index+1])
                if value_list[pos_next]>value_list[pos]:
                    num-=value_list[pos]
                else:
                    num+=value_list[pos]
            else:
                num+=value_list[pos]
        return num
