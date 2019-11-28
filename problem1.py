n= int(input())
a=[]
b=[]
for i in range(n):
  x,y = map(int,input().split())
  a.append(x)
  b.append(y)
c=[]
for i in range(n):
  x=[i for i in range(1,a[i]+1)]
  while(a[i]>=b[i]):
    y=[]
    for j in range(len(x)):
      if (j+1)%b[i] == 0:
        y.append(x[j])
    x=y
    a[i]=len(x)
  c.append(x[0])
for i in c:
  print(i)
