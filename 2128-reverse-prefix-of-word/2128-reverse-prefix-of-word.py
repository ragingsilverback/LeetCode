class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        for j in range(len(word)):
            if word[j]==ch:
                i = 0
                ans = list(word)
                ans[:j+1] = reversed(ans[:j+1])
                return "".join(ans)

        return word

        
        