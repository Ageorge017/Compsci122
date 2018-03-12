from classes import Stack
def main():
    x=int(input("Enter a number"))
    BinaryStack=ToBinary(x)
def ToBinary(n):
    BinStack=Stack()
    L=[]
    while n!=0:
        x=n%2
        BinStack.push(x)
        n=n//2
    while not BinStack.isEmpty():
        L.append(str(BinStack.peek()))
        BinStack.pop()
    NewBinLst=''.join(L)
    print(NewBinLst)
    
    

        
        
