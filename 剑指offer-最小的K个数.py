# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        res = []#返回结果
        if k<=len(tinput):#当k值小于或等于tinput长度时
            for i in range(k):#循环k次
                res.append(min(tinput))#每次取最小
                tinput.remove(min(tinput))#移除当前最小
            return res
        return []#当k值大于tinput长度时,返回空