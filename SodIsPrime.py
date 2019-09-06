def sumOfDigs(t):
  s=0
  while(t>0):
    d=t%10
    s+=d
    t=t//10
  return s 
def isPrime(n):
  i=2
  t=0
  while(i<=n/2):
    if n%i==0 :
      t=1
      break
    i += 1
  if t==0 and n!=1 :
    return 1
  else:
    return 0
a,b= map(int,input().split())
d=0
for i in range(a,b+1):
  c = sumOfDigs(i)
  if isPrime(c):
    d+=1
print(d)    
