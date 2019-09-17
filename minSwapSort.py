def minSwaps(arr): 
    n = len(arr) 
    arrpos = [*enumerate(arr)]
    #print(arr,arrpos,'@')
    arrpos.sort(key = lambda i:i[1]) 
    vis = {k:False for k in range(n)}
    #print(arrpos,arr,vis,'*')
    ans = 0
    for i in range(n): 
        if vis[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i 
        while not vis[j]:
            vis[j] = True
            #print(i,j,'#')
            j = arrpos[j][0]
            #print(j,'%')
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1)
            #print('ans',ans)
    return ans 
n=int(input())
a=list(map(int,input().split()))
print(minSwaps(a)) 
