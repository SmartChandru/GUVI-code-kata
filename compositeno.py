n=int(input())
i=2
t=0
while(i<=n/2):
  if n%i==0 :
    t=1
    break
  i += 1
if t==1 :
  print("yes")
else:
  print("no")
