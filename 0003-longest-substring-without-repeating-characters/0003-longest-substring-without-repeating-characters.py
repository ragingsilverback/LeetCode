class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxlen = 0
        dic = {}

        while(right<len(s)):
            if s[right] in dic:
                left = max(left,dic[s[right]] + 1)

            dic[s[right]] = right
            maxlen = max(maxlen,right-left+1)
            right +=1

        return maxlen

        
        