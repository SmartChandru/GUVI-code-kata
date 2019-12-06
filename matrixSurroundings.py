m,n = map(int,input().split())
a=[]
for i in range(m):
  a.append(list(map(int,input().split())))
b=[]
for i in range(m):
  t=[]
  for j in range(n):
    if i==0 and j==0:
      t.append(a[i+1][j]+a[i][j+1]+a[i+1][j+1])
    elif i==0 and j==n-1:
      t.append(a[i][j-1]+a[i+1][j]+a[i+1][j-1])
    elif i==m-1 and j==0:
      t.append(a[i-1][j]+a[i][j+1]+a[i-1][j+1])
    elif i==m-1 and j==n-1:
      t.append(a[i][j-1]+a[i-1][j]+a[i-1][j-1])
    elif i==0 :
      t.append(a[i][j-1]+a[i][j+1]+a[i+1][j+1]+a[i+1][j]+a[i+1][j-1])
    elif j==0 :
      t.append(a[i-1][j]+a[i+1][j]+a[i+1][j+1]+a[i][j+1]+a[i-1][j+1])
    elif i==m-1 :
      t.append(a[i][j-1]+a[i][j+1]+a[i-1][j+1]+a[i-1][j]+a[i-1][j-1])
    elif j==n-1 :
      t.append(a[i-1][j]+a[i+1][j]+a[i-1][j-1]+a[i][j-1]+a[i+1][j-1])
    else:
      t.append(a[i][j-1]+a[i][j+1]+a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1])
  b.append(t)
for i in b:
  print(*i)
