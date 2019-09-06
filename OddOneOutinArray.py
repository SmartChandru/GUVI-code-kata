n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
  k=a[i]
  t=0
  for j in range(0,n):
    if k==a[j] and i!=j :
      break
    if k!=a[j]:
      t+=1
    #print(k,t,i,j," *")  
  if t==n-1 :
    print(k)
    break
