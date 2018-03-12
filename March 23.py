def main():
    L=[]
    x=GetNumbers(L)
    y=largestNum(x)
    print(y)
    
    
    

def GetNumbers(L):
    x=eval(input("Enter a number. Enter -999 to stop"))
    if x!=-999:
        L.append(x)
        GetNumbers(L)
    return L

def largestNum(NumList):
    largest=NumList[0]
    for i in NumList:
        if i > largest:
            largest=i
    return largest
    

    



    

        
        


            

    
