x = input()
n = int(x)
t=0
for i in range(1,n+1):
  j = str(i)
  k = [int(l) for l in j]
  m = [str(k[r]) for r in range(len(k)-1,-1,-1)]
  y = "".join(m)
  if j==y:
    print(j,y)  
    t+=1
print(t)
