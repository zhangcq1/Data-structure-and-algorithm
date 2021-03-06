#-----------------------------逆波兰计算器--------------------------------
class Stack():#定义一个栈
    def __init__(self,):
        self.stack = []
    def push(self,data):#入栈
        self.stack.append(data)
    def pop(self):#出栈
        return self.stack.pop()
    def is_empty(self):#是否栈空
        return not len(self.stack)
    def top(self):#栈顶元素
        if self.is_empty():
            return None
        return self.stack[-1]




class InversPolishCalculator(object):#逆波兰计算器

    def deal(self,exspression):#主程序,传入中缀表达式,返回结果
        list_expression = self.get_list_expression(exspression)
        stack = Stack()  # 实例化栈
        for ele in list_expression:  # 处理逆波兰表达式
            if ele.replace('.','').isdigit():  # 是数字压入栈
                stack.push(ele)
            else:  # 是运算符进行运算,用次顶元素,和栈顶元素
                ret = self.operation(ele, float(stack.pop()), float(stack.pop()))
                stack.push(ret)
        return '%.2f'% stack.pop()#返回结果

    def operation(self,sign, num2, num1):  # 定义算法
        if sign == '*':
            return num1 * num2
        if sign == '/':

            return num1/num2
        if sign == '+':
            return num1 + num2
        if sign == '-':
            return num1 - num2

    def deal_str(self,exspression):#处理中缀表达式字符串,转为列表形式方便计算
        status = 0
        res = ''
        exspression = exspression.strip().replace(' ','')
        for ele in exspression:
            if ele.isdigit() or ele =='.':
                if status == 1:
                    res =res.strip(' ')
                    res = res + ele + ' '
                else:
                    status = 1
                    res= res+ele+' '
            else:
                status = 0
                res = res + ele + ' '
        return res.strip().split(' ')

    def get_list_expression(self,exspression):#将中缀表达式列表形式转后缀
        lst = self.deal_str(exspression)
        s1 = Stack()
        s2 = Stack()
        for ele in lst:
            if ele.replace('.','').isdigit():
                s2.push(ele)
            else:
                self.deal_symbol(ele,s1,s2)
        while not s1.is_empty():
            s2.push(s1.pop())
        res = []
        while not s2.is_empty():
            res.append(s2.pop())
        return res[::-1]

    def deal_symbol(self,ele,s1,s2):#处理符号入栈出栈问题
        if s1.is_empty() or s1.top() == '(' or ele == '(':
            s1.push(ele)
        elif ele == ')':
            while s1.top() != '(':
                s2.push(s1.pop())
            s1.pop()
        elif self.get_priority(ele) > self.get_priority(s1.top()):
            s1.push(ele)
        else:
            s2.push(s1.pop())
            self.deal_symbol(ele,s1,s2)

    def get_priority(self,sign):#获取符号优先级
        if sign=='*' or sign=='/':
            return 2
        elif sign=='+' or sign=='-':
            return 1



if __name__ == '__main__':
    exspression = input('请输入计算公式:')
    Calculator = InversPolishCalculator()
    ret = Calculator.deal(exspression)
    print('计算结果:',ret)
    input()
