#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
 @Project       :project
 @Environment   :PyCharm
 @File          :test_sf.py
 @Author        :雪沐
 @Date          :2020/10/27 下午8:37
 """
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}
        for i in range(len(nums)):
            if hashset.get(target-nums[i]) is not None :
                return [hashset.get(target-nums[i]),i]
            hashset[nums[i]]=i

