n= int(input())
a=[]
for i in range(n):
  b= input()
  a.append(b)
s=0
for i in range(len(a[0])):
  for j in range(n-1):
    if a[j][i]==a[j+1][i] :
      t=0
    else:
      t=1
      break
  if t==0:
    s+=1
    #print(s,t,i,j)
  else:
    #print(s,t,i,j)
    break
for i in range(s):
  print(a[0][i],end="")
