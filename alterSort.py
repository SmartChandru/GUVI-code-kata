n=int(input())
ls= list(map(int,input().split()))
if n%2==0 :
  for i in range(0,n-3,2):
    for j in range(i+2,n-1,2):
      if ls[i]>ls[j] :
        ls[i],ls[j] = ls[j],ls[i]
      if ls[i+1]>ls[j+1] :
        ls[i+1],ls[j+1] = ls[j+1],ls[i+1]
else:
  for i in range(0,n-2,2):
    for j in range(i+2,n,2):
      if ls[i]>ls[j] :
        ls[i],ls[j] = ls[j],ls[i]
      if ls[i+1]>ls[j-1] :
        ls[i+1],ls[j-1] = ls[j-1],ls[i+1]
for i in ls:
  print(i,end=" ")
  
'''

n=int(input())
ls= list(map(int,input().split()))
if n%2==0 :
  for i in range(0,n-3,2):
    for j in range(i+2,n-1,2):
      if ls[i]>ls[j] :
        ls[i],ls[j] = ls[j],ls[i]
  for i in range(1,n-2,2):
    for j in range(i+2,n,2):
      if ls[i]>ls[j] :
        ls[i],ls[j] = ls[j],ls[i]
  
else:
  for i in range(0,n-2,2):
    for j in range(i+2,n,2):
      if ls[i]>ls[j] :
        ls[i],ls[j] = ls[j],ls[i]
  for i in range(1,n-3,2):
    for j in range(i+2,n-1,2):
      if ls[i]>ls[j] :
        ls[i],ls[j] = ls[j],ls[i]
        
for i in ls:
  print(i,end=" ")



'''



'''
n=int(input())
ls= list(map(int,input().split()))
for i in range(0,n-2,2):
  for j in range(i+2,n,2):
    if ls[i]>ls[j] :
      ls[i],ls[j] = ls[j],ls[i]
    if ls[i+1]>ls[j-1] and n%2==1 :
      ls[i+1],ls[j-1] = ls[j-1],ls[i+1]
    if ls[i+1]>ls[j+1] and n%2==0 :
      ls[i+1],ls[j+1] = ls[j+1],ls[i+1]
for i in ls:
  print(i,end=" ")

n=int(input())
ls= list(map(int,input().split()))
for i in range(0,n-2,2):
  for j in range(i+2,n,2):
    if ls[i]>ls[j] :
      ls[i],ls[j] = ls[j],ls[i]
for i in range(1,n-3,2):
  for j in range(i+2,n,2):
    if ls[i]>ls[j] :
      ls[i],ls[j] = ls[j],ls[i]
for i in ls:
  print(i,end=" ")

'''
