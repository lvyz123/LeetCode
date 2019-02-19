class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s.isalpha():
            return False
        else:
            p_recov='';p_index=0
            while p_index<len(p):
                if p_index>=len(s):
                    return False
                elif p[p_index]==s[p_index] or p[p_index]=='.':
                    p_recov+=s[p_index]
                elif p_index>0 and p[p_index]=='*':
                    if s[p_index]==s[p_index-1] or p[p_index-1]=='.':
                        p_recov+=s[p_index]
                elif p_index<len(p)-1 and p[p_index+1]=='*':
                    p.replace(p[p_index:p_index+2],'')
                    p_index-=1
                else:
                    return False
                p_index+=1
            if len(s)>len(p):
                return False
            return True
