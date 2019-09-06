def prime(n):
  l=[]
  p=2
  while(n>0):
    i=2
    t=0
    while(i<=p/2):
      if p%i==0 :
        t=1
        break
      i+=1
    if t==0:
      l.append(p)
      n-=1
    p+=1
  return l
n=int(input())
l=prime(n)
s=0
for i in l:
  s+=i
  print(s,end=" ")
  
