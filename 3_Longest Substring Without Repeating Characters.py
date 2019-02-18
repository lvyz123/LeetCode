class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_index=0;last_index=1
        if s!='':
            cand_str=s[0]
        else:
            return 0
        while first_index<len(s)-1:
            while last_index<len(s) and (s[last_index] not in s[first_index:last_index]):
                last_index+=1
            curr=s[first_index:last_index]
            if len(curr)>len(cand_str):
                cand_str=curr
            if last_index==len(s):
                break
            else:
                first_index+=curr.index(s[last_index])+1
        return len(cand_str)
