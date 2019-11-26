def isP(n):
  s = str(n)
  n = len(s)
  t=1
  for i in s:
    if i not in ['2','3','5','7']:
      t=0
      break
  return t
n= int(input())
t=0
a=[]
c=1
while(t<n):
  #print(a,c,t,n)
  if isP(c):
    a.append(c)
    t+=1
  c+=1
print(a[len(a)-1])  
