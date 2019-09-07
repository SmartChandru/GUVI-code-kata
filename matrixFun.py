m,n=map(int,input().split())
a=[]
b=[]
for i in range(m):
  t=list(map(int,input().split()))
  a.append(t)
for i in range(m):
  for j in range(n):
    if a[i][j] == 0 :
      for k in range(n):
        a[i][k] = 0
      b.append(j)  
      break
for i in b:
  for k in range(m):
    a[k][i] = 0
for i in range(m):
  for j in range(n):
    print(a[i][j],end=" ")
  print()
