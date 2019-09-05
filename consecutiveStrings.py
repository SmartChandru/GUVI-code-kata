n,k=map(int,input().split())
s=0
ls=[]
for i in range(0,n):
  x = input() 
  ls.append(x)
#print(ls)  
for i in range(0,n-k+1):
  f=1
  for j in range(i+1,n):
    if ls[i]!=ls[j]:
      break
    else:
      f+=1
   # print(i,j,f,k," ")
  if f==k :
    s=1
 # print(i,j,f,k," |")  
if s==1:
  print("yes")
else:
  print("no")
