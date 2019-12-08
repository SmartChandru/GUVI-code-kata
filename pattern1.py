n=int(input())
x=n
y=n+1
t=1
a=[]
for i in range(1,2*n):
  b=[]
  if i<=n:
    y-=1
  else:
    y+=1
  x=y
  #print(i,y,'*')
  for j in range(1,2*n):
    #print(i,j,x)
    b.append(x)
    if j<t or j>2*n-1-t:
      x=y 
    elif j<n:
      x-=1
    else:
      x+=1
  #print('t',t)    
  if i<n:
    t+=1
  else:
    t-=1
  a.append(b)
for i in a:
  print(*i)
    
