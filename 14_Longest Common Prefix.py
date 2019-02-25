class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)>0:
            match=strs[0];
        else:
            return ''
        for string in strs[1:]:
            for i in range(min(len(match),len(string))):
                if string[i]!=match[i] and i<=len(match)-1:
                    match=match[:i]
                    pre_match=match
                    break
            if len(match)>len(string):
                match=match[:len(string)]
        return match
