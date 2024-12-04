class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i,j = 0,0
        while i<len(str1) and j<len(str2):
            nextChar = chr((ord(str1[i])-ord('a')+1)%26 + ord('a'))
            if str1[i]==str2[j] or (nextChar==str2[j]):
                i += 1
                j += 1
            else:
                i += 1

        print([i,j])
        if(j==len(str2)):
            return True
        else:
            return False