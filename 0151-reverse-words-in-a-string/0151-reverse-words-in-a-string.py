class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        a = [word for word in l if word!='']
        
        i,j = 0,len(a)-1
        while(i<j):
            a[i],a[j] = a[j],a[i]
            i +=1
            j -=1

        return " ".join(a)
        
        
        