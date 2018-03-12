class Stack:
    def __init__(self,itemList=[]):
        self.items=itemList
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    def push(self, item):
        self.items.append(item)
        return 0
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1:][0]
    def size(self):
        return len(self.items)
