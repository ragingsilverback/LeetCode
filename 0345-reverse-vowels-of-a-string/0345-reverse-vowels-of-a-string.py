class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        a = set(vowels)
        l = list(s)

        i,j = 0,len(s)-1
        while(i<j):
            while(i<j and l[i] not in a):
                i +=1
            while(i<j and l[j] not in a):
                j -=1
            l[i],l[j] = l[j],l[i]
            i +=1
            j -=1

        return "".join(l)

        