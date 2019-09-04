def dist(a1,b1,a2,b2) :
  return (a2-a1)**2 + (b2-b1)**2
  
def isEqSides(d1,d2,d3,d4):
  if d1==d2 and d1==d3 and d1==d4 :
    return True
  else:
    return False

def isEqDiag(d1,d2):
  if d1==d2 :
    return True 
  else: 
    return False

def isRight(d1,d2):
  if 2*d1 == d2 :
    return True 
  else:    
    return False

  
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())

da= dist(x1,y1,x2,y2)
db= dist(x2,y2,x3,y3)
dc= dist(x3,y3,x4,y4)
dd= dist(x4,y4,x1,y1)
d1= dist(x1,y1,x3,y3)
d2= dist(x2,y2,x4,y4)
if isEqSides(da,db,dc,dd):
  if isEqDiag(d1,d2):
    if isRight(da,d1):
      print("yes")
    else: 
      print("no")
  else: 
    print("no")
else: 
  print("no")    
    
 
 
