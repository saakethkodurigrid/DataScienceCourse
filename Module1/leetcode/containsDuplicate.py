#https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        for key in mp:
            if mp[key]>1:
                return True
        return False

        