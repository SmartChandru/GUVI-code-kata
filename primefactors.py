n=int(input())
if n%2 == 0 : 
  print(2,end=" ") 
  n = n / 2
for i in range(3,int(n/2),2):
  if n % i== 0: 
    print(i,end=" ") 
    n = n / i 

