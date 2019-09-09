a = list(input().split())
n = len(a)
for i in range(n):
  a[i] = sorted(a[i])
for i in range(n):
  for j in a[i]:
    print(j,end="")
  print(end=" ")  
