str = input()
#print(str)
ls = str.split()
#print(ls)
n = len(ls)
#print(n)
for i in range(0,n-1,2):
  ls[i],ls[i+1]=ls[i+1],ls[i]
#print(ls)
for i in ls:
    print(i,end=" ")
