# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []#栈
    def IsPopOrder(self, pushV, popV):
        # write code here
        index = 0  #出栈队列popV下标,从0到len(popV)-1
        for ele in pushV:#循环入栈的数据
            if ele == popV[index]:#判断入栈元素是否等于当前出栈队列的元素
                index += 1#如果等于,下标后移,继续寻找下一个
                if index == len(popV):#通过index判断,是否寻找完毕,是返回True,否继续下一步
                    return True
                while self.stack[0] == popV[index]:#当寻找的当前出栈元素等于栈顶元素时
                    self.stack.pop(0)#出栈,
                    index+=1#下标后移,继续寻找下一个
                    if index==len(popV):#通过index判断,是否寻找完毕,是返回True,否继续下一步
                        return True
            else:#如果不等于将元素入栈,做后续处理
                self.stack.insert(0, ele)
        return False
        #如果循环结束没有返回True,说明popV没有寻找完毕,即index<len(popV),
        # 即popV不是pushV的出栈队列

lst = [1,2,4,5]
lst.remove(min(lst))
print(lst)