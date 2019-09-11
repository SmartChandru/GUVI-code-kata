import fractions 
def lcm(n): 
    ans = 1    
    for i in n: 
        ans = (ans * i)/fractions.gcd(ans, i)         
    return ans
n= int(input())
a= list(map(int,input().split()))
x= lcm(a)
print(x)
