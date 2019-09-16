n,k=map(int,input().split())
a=list(map(int,input().split()))
t=0
for i in range(n-1):
  for j in range(i+1,n):
    if a[i]<a[j]:
      a[i],a[j]= a[j],a[i]
for i in a:
  t+= k//i
  k%=i
print(t)
