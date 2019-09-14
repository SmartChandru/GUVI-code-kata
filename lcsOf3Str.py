a,b,c= input().split()
m= len(a)
n= len(b)
o= len(c)
s=0
if m<n and m<o:
  t=m
elif n<o:
  t=n
else:
  t=o
for i in range(t):
  if a[i]==b[i] and b[i]==c[i]:
    print(a[i],end='')
    s=1
if s==0:
  print(-1)
