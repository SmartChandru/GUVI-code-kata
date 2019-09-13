n=int(input())
a=[]
for i in range(n):
  b= input()
  a.append(b)
c=[]
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in range(n):
  t=0
  for j in a[i]:
    if j in vowels:
      t+=1
  c.append(t)
for i in range(n-1):
  for j in range(i+1,n):
    if c[i]<c[j]:
      c[i],c[j]=c[j],c[i]
      a[i],a[j]=a[j],a[i]
for i in a:
  print(i)  
  
