def prime(m,n):
  l=0
  for j in range(m,n+1):
    i=2
    t=0
    while(i<=j/2):
      if j%i==0 :
        t=1
        break
      i+=1
    if t==0:
      l+=1
  return l
m,n=map(int,input().split())
l=prime(m,n)
print(l)

