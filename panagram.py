def rev(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
def anagram(x,y):
  t=1
  for i in x:
    if i not in y :
      t=0
      break
  for i in y:
    if i not in x :
      t=0
      break
  return t
a,b = input().split()
if (a==rev(a) or b==rev(b)) and anagram(a,b):
  print(1)
else:
  print(0)
