n=int(input())
l=[]
for i in range(0,n):
  t= list(map(int,input().split()))
  l.append(t)
#print(l)
s=0
a=1
b=1
for i in range(0,n):
  for j in range(0,n):
    if i==j :
      a *= l[i][j]
    if i+j == n-1 :
      b *= l[i][j]
s=a+b
print(s)
