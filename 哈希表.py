#-------------------------------哈希表的实现----------------------------------
class HashTab(object):
    def __init__(self,):
        pass
class HashTabHead(object):
    def __init__(self,):
        self.next = None
    def add(self,element):
        if self.next == None:
            self.next = element
        else:
            pointer = self.next
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = element
    def delete(self):
        pass
    def show(self):
        data = []
        pointer = self.next
        while pointer.next != None:
            data.append(pointer.id)
            pointer = pointer.next
        data.append(pointer.id)
        print(data)
class HashTabElement(object):
    def __init__(self,id,):
        self.id = id
        self.next = None
class main():
    def __init__(self,**args):
        print(args)

if __name__ == '__main__':
    main(a=1)
    # head = HashTabHead()
    # ele1 = HashTabElement(1)
    # ele2 = HashTabElement(2)
    # ele3 = HashTabElement(3)
    # ele4 = HashTabElement(4)
    # ele5 = HashTabElement(5)
    # ele6 = HashTabElement(6)
    # head.add(ele1)
    # head.add(ele2)
    # head.add(ele3)
    # head.add(ele4)
    # head.add(ele5)
    # head.add(ele6)
    # head.show()