class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        max_area=0;larger_index=[];l=len(height)
        sorted_height=sorted(height,reverse=True)
        for a_value in sorted_height:
            if a_value*l<max_area:
                break
            a_index=height.index(a_value)
            if len(larger_index)>0:
                curr_area=max(abs(max(larger_index)-a_index),abs(min(larger_index)-a_index))*a_value
                if curr_area>max_area:
                    max_area=curr_area
            larger_index.append(a_index)
            height[a_index]=0
        return max_area
