class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {}
        if bills[0]!=5:
            return False
        total = 0
        for bill in bills:
            change = bill - 5
            if change>0:
                if change>total:
                    return False
                if dic.get(change,0)>0:
                    dic[change] -= 1
                else:
                    for denom in [20,10,5]:
                        while change >= denom and dic.get(denom,0)>0:
                            change = change - denom
                            dic[denom] -= 1
                            if change==0:
                                break
                    if change != 0:
                        return False

            dic[bill] = dic.get(bill,0) + 1
            total += 5
        return True




        