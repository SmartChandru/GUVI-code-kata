m=int(input())
n=[]
a=[]
x=[]
for i in range(m):
  o=int(input())
  b=list(map(int,input().split()))
  l=int(input())
  n.append(o)
  a.append(b)
  x.append(l)
for i in range(m):
  for j in range(len(a[i])-1):
    for k in range(j+1,len(a[i])):
      if a[i][j] > a[i][k]:
        a[i][j] , a[i][k] = a[i][k] , a[i][j]
#print(a)
c=[]
for i in a:
  d=[]
  for j in i:
    if j not in d:
      d.append(j)
      #print(d)
  c.append(d)
#print(c)
for i in range(m):
  #print(i,t)
  print(c[i][x[i]-1])
