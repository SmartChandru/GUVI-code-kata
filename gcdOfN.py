def gcd(x, y): 
  while(y): 
    x, y = y, x % y 
  return x 
n= int(input())
a= list(map(int,input().split()))
n= len(a)
x=a[0] 
y=a[1] 
g=gcd(x,y) 
for i in range(2,n): 
    g=gcd(g,a[i]) 
print(g)
