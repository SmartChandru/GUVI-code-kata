n= int(input())
a= list(map(int,input().split()))
max=1
for i in range(0,n-1):
  t=1
  for j in range(i+1,n):
    if a[i]==a[j]:
      t+=1
      #print(i,j,t,a[i],a[j])
    else:
      break
    if t>max:
      max=t
print(max)
