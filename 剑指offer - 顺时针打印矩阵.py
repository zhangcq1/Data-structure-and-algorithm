# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix:
            res = []
            left, right = 0, len(matrix[0])#获取左右长度,即数组中的每个数组长度
            top, bottom = 0, len(matrix)#获取上下度,即数组中数组个数
            while left < right and top < bottom:
                #当左数值小于右数值,和上数值小于下数值,说明没有打印结束,继续打印
                for i in range(left, right):#从左到右
                    res.append(matrix[top][i])
                for i in range(top + 1, bottom):#从上到下
                    res.append(matrix[i][right - 1])

                if top == bottom - 1:#如果上下是同一行,说明打印结束,直接退出,否则继续执行
                    break
                lst1 = [x for x in range(left, right - 1)]
                #直接range(1,0,-1),取的是1,不是0,导致结果错误
                lst1.reverse()
                for i in lst1:
                    res.append(matrix[bottom - 1][i])

                if left == right - 1:##如果上下是同一列,说明打印结束,直接退出,否则继续执行
                    break
                lst2 = [x for x in range(top + 1, bottom - 1)]
                lst2.reverse()
                for i in lst2:
                    res.append(matrix[i][left])

                left += 1
                top += 1
                right -= 1
                bottom -= 1
            return res
        else:#空矩阵返回空数组
            return []
            # write code here