def rev(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

a = list(input().split())
n = len(a)
for i in range(n):
  a[i] = rev(a[i])
  print(a[i], end=" ")
