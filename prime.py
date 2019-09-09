n=int(input())
i=2
while i<=n:
  t=0
  for j in range(2,int(i/2)+1):
    if i%j == 0:
      t=1
      break
  if t==0:
    print(i, end=" ")
  i+=1
