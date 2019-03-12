class Solution:
    def letterCombinations(self, digits):
        str_list=[];letter_list_rec=[0]*8;
        letter_ref=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'];
        for idx,str_ref in enumerate(letter_ref):
            letter_list_rec[idx]=list(set(str_ref))
        for digit in digits:
            num=int(digit);
            letter_list=letter_list_rec[num-2];
            if str_list:
                for cur_str in str_list:
                    str_list.remove(cur_str);
                    for letter in letter_list:
                        cur_str+=letter;
                        str_list.append(cur_str);
                        cur_str=cur_str[:-1];
            else:
                str_list=letter_list;
        return str_list
