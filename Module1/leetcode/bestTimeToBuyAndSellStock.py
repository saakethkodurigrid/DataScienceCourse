#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi=prices[0]
        ans=0
        for i in prices:
            if i > maxi:
                maxi=i
                ans=max(ans,maxi-mini)
            if i < mini:
                mini=i
                maxi=i
        return ans