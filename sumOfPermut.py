def permutation(lst): 
  if len(lst) == 0: 
      return [] 
  if len(lst) == 1: 
      return [lst] 
  l = [] 
  for i in range(len(lst)): 
     m = lst[i] 
     remLst = lst[:i] + lst[i+1:] 
     for p in permutation(remLst): 
         l.append([m] + p) 
  return l

n = list(input())
l=permutation(n)
s=0
for i in l:
    s += int("".join(i))
print(s)
