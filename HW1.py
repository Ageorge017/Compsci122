def NumTwo():
    m=eval(input("M = "))
    n=eval(input("N = "))
    sum = 0
    for i in range(m,n+1):
        sum+=i
    print(sum)

def NumThree():
    m=eval(input("M = "))
    n=eval(input("N = "))
    return m,n

def PrintNumThree():
    a,b=NumThree()
    sum=0
    for i in range(a,b+1):
        sum+=i
    print(sum)
    

def NumFour():
    L=[]
    num=int(input("Enter a positive integer or 0 to stop= "))
    sum=0
    while num >0:
        L.append(num)
        sum+=num
        num=int(input("Enter another number= "))
    print(sum)

def NumFive():
    L=[]
    num = int(input("Enter a positive integer or 0 to stop= "))
    while num>0:
        L.append(num)
        num=int(input("Enter another number= "))
    print(max(L))

def NumSix():
    def main():
        win = GraphWin("Draw a Triangle")
        win.setCoords(0.0, 0.0, 10.0, 10.0)
        message = Text(Point(5, 0.5), "Click on three points")
        message.draw(win)
        p1 = win.getMouse()
        p1.draw(win)
        p2 = win.getMouse()
        p2.draw(win)
        p3 = win.getMouse()
        p3.draw(win)
        triangle = Polygon(p1,p2,p3)
        triangle.setFill("peachpuff")
        triangle.setOutline("cyan")
        triangle.draw(win)
        message.setText("Click anywhere to quit.")
        win.GetMouse()
