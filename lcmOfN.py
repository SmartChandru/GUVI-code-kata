def gcd(x, y): 
  while(y): 
    x, y = y, x % y 
  return x 
def lcm(n1, n2): 
  g = gcd(n1,n2) 
  lcm = int((n1 * n2)/g) 
  return lcm 

n= int(input())
a= list(map(int,input().split()))
num1 = a[0] 
num2 = a[1] 
l = lcm(num1, num2) 
  
for i in range(2, n): 
    l = lcm(l, a[i])
print(l)
