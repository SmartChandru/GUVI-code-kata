import math
n1,n2 = map(int,input().split())
sq = int(math.sqrt(n1 * n2))
if((sq * sq) == n1 * n2):
  print('yes')
else:
  print('no')
