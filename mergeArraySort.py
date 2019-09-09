n= int(input())
a=[]
m=0
for i in range(n):
  b = list(map(int,input().split()))
  a.extend(b)
  m += len(b)
#print(a,m)

for i in range(0,m-1):
  for j in range(i+1,m):
    if a[i]>a[j]:
      a[i], a[j] = a[j], a[i]
for i in a:
  print(i,end=" ")
