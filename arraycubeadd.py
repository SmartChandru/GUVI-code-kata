n=int(input())
a=list(map(int,input().split()))
t=0
for i in range(0,n-1):
  for j in range(i+1,n):
    for k in range(0,n):
      if a[i]+a[j]==a[k] :
        t+=1
print(t)    
