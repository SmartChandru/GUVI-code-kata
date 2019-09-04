n=int(input())
ls= list(map(int,input().split()))
max=min=ls[0]
l=h=1
for i in range(1,n) :
  if(ls[i]>max):
   max=ls[i]
   h=i+1
for i in range(1,n) :
  if(ls[i]<min):   
   min=ls[i]
   l=i+1
print(l,h)
