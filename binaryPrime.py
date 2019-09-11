def isPrime(n): 
  if n <= 1 :  return False
  if n <= 3 :  return True 
  if n%2 == 0 or n%3 == 0 : return False 
  for i in range(5,n//2,6):
    if n%i == 0 or n%(i+2) == 0 : 
      return False 
  return True 
 
def setBits(n): 
    return bin(n)[2:].count('1')

a,b = map(int, input().split())
c=0
for i in range(a, b+1): 
  t = setBits(i)
  if isPrime(t) : 
    c += 1
print(c) 
