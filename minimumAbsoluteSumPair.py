n= int(input())
a= list(map(int,input().split()))
x=0
y=0
t=0
min=1666666666
for i in range(n-1):
  for j in range(i+1,n):
    if a[i]<0 and a[j]>0 or a[i]>0 and a[j]<0:
      t = abs( a[i] + a[j] )
     # print(i,j,a[i],a[j],t)
      if t<min:
        min=t
        x=a[i]
        y=a[j]
      #  print(i,j,a[i],a[j],t,"*")
print(x,y)
