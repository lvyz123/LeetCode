class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        roman_num=''
        symbol_list=['I','V','X','L','C','D','M']
        value_list=[1,5,10,50,100,500,1000,5000]
        while num>0:
            if num in value_list:
                roman_num+=symbol_list[value_list.index(num)]
                break
            else:
                value_list.append(num)
            value_list=sorted(value_list);num_pos=value_list.index(num);pre_num=num
            if num_pos%2==0:
                if num<value_list[num_pos-1]+4/5*(value_list[num_pos+1]-value_list[num_pos-1]):
                    roman_num+=symbol_list[num_pos-1]*(num//value_list[num_pos-1])
                    num-=value_list[num_pos-1]*(num//value_list[num_pos-1])
                else:
                    roman_num+=(symbol_list[num_pos-2]+symbol_list[num_pos])
                    num-=(value_list[num_pos+1]-value_list[num_pos-2])
            else:
                if num<value_list[num_pos-1]+3/4*(value_list[num_pos+1]-value_list[num_pos-1]):
                    roman_num+=symbol_list[num_pos-1]*(num//value_list[num_pos-1])
                    num-=value_list[num_pos-1]*(num//value_list[num_pos-1])
                else:
                    roman_num+=(symbol_list[num_pos-1]+symbol_list[num_pos])
                    num-=(value_list[num_pos+1]-value_list[num_pos-1])
            value_list.remove(pre_num)
        return roman_num
