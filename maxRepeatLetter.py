a= input()
n=len(a)
max=0
for i in range(n):
  c=1
  for j in range(n):
    if a[i] == a[j] and i!=j:
      c+=1
  if c>max:
    max=c
    b= a[i]
print(b)
