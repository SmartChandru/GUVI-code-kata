def count(a, n, k): 
  s = 0
  i = 0
  while (i < n): 
    if (a[i] > k): 
      i = i + 1
      continue
    c = 0
    while (i < n and a[i] <= k):     
      i = i + 1
      c = c + 1
      #print(i,c,s)
    s = s + ((c*(c + 1))//2)
    #print(i,c,s,"*")
  return (n*(n + 1)//2 - s)
n,k = map(int,input().split())
a = list(map(int,input().split()))
print(count(a, n, k)) 
  
