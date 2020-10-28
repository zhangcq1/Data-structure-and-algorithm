# ------------------------第一种--------------------------
class Solution:
    def __init__(self):
        self.firstQueue = []#模拟第一个栈
        self.secondQueue = []#模拟第二个栈
    def push(self, node):#向队列中插入数据时,就先向第一个栈存放数据
        self.firstQueue.insert(0, node)#模拟栈的操纵,新插入的值在栈顶
        # write code here
    def pop(self):
        #向队列中取数据时,就是将第一个栈中的数据取出存放到第二个栈中,
        # 使数据反转达到数列效果,如果第二个栈中不为空,继续取数据,如果为空,
        # 就继续反转栈一数据,存到栈二中继续取值
        if self.secondQueue:
            res = self.secondQueue.pop(0)#模拟栈的取值,取栈顶元素
            return res
        else:
            while self.firstQueue:
                #主要逻辑,将栈一数据,存到栈二中进行取值操纵
                ele = self.firstQueue.pop(0)
                self.secondQueue.insert(0, ele)

            res = self.secondQueue.pop(0)
            return res


# ------------------------第二种--------------------------
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.queue = []
    def push(self, node):
        self.queue.append(node)
        # write code here
    def pop(self):
        res = self.queue.pop(0)
        return res
        # return x