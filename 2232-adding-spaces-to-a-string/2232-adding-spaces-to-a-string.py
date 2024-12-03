class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        # spaces_set = set(spaces)
        # for i in range(len(s)):
        #     if i in spaces:
        #         ans = ans + " "
        #     ans = ans + s[i]
        point = 0
        for i in spaces:
            ans = ans + s[point:i]
            ans = ans + " "
            point = i

        ans = ans + s[point:]


        return ans

        