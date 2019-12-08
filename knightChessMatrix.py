a=[]
for i in range(4):
  a.append(list(input()))
n=int(input())
b=[]
c=[]
d=[0,1,2,3]
for i in range(n):
  x,y = map(int,input().split())
  b.append(x)
  c.append(y)
e=[]  
for k in range(n):
  i=b[k]
  j=c[k]
  t=0
  if i+1 in d and j+2 in d:
    if a[i+1][j+2]=='.' and a[i][j]!='#':
      t+=1
  if i+2 in d and j+1 in d:
    if a[i+2][j+1]=='.' and a[i][j]!='#':
      t+=1
  if i-1 in d and j+2 in d:
    if a[i-1][j+2]=='.' and a[i][j]!='#':
      t+=1
  if i+2 in d and j-1 in d:
    if a[i+2][j-1]=='.' and a[i][j]!='#':
      t+=1
  if i+1 in d and j-2 in d:
    if a[i+1][j-2]=='.' and a[i][j]!='#':
      t+=1
  if i-2 in d and j+1 in d:
    if a[i-2][j+1]=='.' and a[i][j]!='#':
      t+=1
  if i-1 in d and j-2 in d:
    if a[i-1][j-2]=='.' and a[i][j]!='#':
      t+=1
  if i-2 in d and j-1 in d:
    if a[i-2][j-1]=='.' and a[i][j]!='#':
      t+=1
  if t==0:
    e.append(-1)
  else:  
    e.append(t)
for i in e:
  print(i)
