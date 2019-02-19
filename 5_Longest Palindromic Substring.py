class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)>0:
            palin_str=s[0]
        else:
            return ''
        for first_index in range(len(s)-1):
            if s[first_index] in s[first_index+1:]:
                end_index=s[first_index+1:].index(s[first_index])+first_index+1
                while s[first_index] in s[end_index:]:
                    curr_str=s[first_index:end_index+1]
                    if curr_str[::-1]==curr_str and len(curr_str)>len(palin_str):
                        palin_str=curr_str
                    if s[end_index] in s[end_index+1:]:
                        end_index=s[end_index+1:].index(s[first_index])+end_index+1
                    else:
                        break
        return palin_str
