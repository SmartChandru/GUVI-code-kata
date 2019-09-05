a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())
d = a1*(b2-b3) + a2*(b3-b1) + a3*(b1-b2)
if d == 0 :
	print("yes")
else:
	print("no")
