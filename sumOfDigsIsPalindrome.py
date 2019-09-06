n=int(input())
t=n
s=0
while(t>0):
  d=t%10
  s+=d
  t=t//10
r=0
t=s
while(t>0):
  d=t%10
  r=r*10+d
  t=t//10
if s==r :
  print("YES")
else:
  print("NO")
  
