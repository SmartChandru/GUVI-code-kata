a = input()
b= []
n= len(a)
for i in range(n):
  if a[i] == '(':
    b.append(a[i])
  if a[i] == ')':
    b.pop()
if len(b)==0 :
  print("yes")
else:
  print("no")
