# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = [] #栈
        self.minstack = []#辅助栈
    def push(self, node):
        self.stack.insert(0, node)#将数据入栈
        if self.minstack==[]:#辅助栈为空时,直接将当前元素加到最小值栈中
            self.minstack.insert(0, node)
        else:#如果当前栈不为空,判断当前元素是否比小于等于最小值,如果小于,入栈
            if node<=self.minstack[0]:
                self.minstack.insert(0, node)
        # write code here
    def pop(self):
        if self.minstack[0]==self.stack[0]:#出栈时,判断两栈栈顶元素是否相等,如果相等同时出栈
            self.minstack.pop(0)
            return self.stack.pop(0)
        else:#如果不等存储栈出栈即可,说明最小元素并未pop出去,故辅助栈不做操作
            return self.stack.pop(0)
        # write code here
    def top(self):
        return self.stack[0]#顶部元素
        # write code here
    def min(self):
        return self.minstack[0]#最小值即辅助栈栈顶元素
        # write code here