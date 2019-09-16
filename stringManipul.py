a= list(input().split('#'))
b= list(input().split('#'))
m = [int(a[i]) for i in range(1,len(a))]
n = [int(b[i]) for i in range(1,len(b))]
x=0
y=0
for i in m:
  x += i
for i in n:
  y += i
if x>y:
  print(a[0])
else:
  print(b[0])
