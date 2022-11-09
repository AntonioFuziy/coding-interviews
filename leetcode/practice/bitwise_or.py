class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        ans = tmp = set()                                                                   
        for n in arr:                           
            tmp = {num|n for num in tmp} | {n}
            ans |= tmp                           
        return len(ans) 