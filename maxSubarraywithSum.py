def maxlen(a,n): 
    max_len = 0
    for i in range(n): 
        s = 0
        for j in range(i, n): 
            s += a[j] 
            if s == 0: 
                max_len = max(max_len, j-i + 1) 
    return max_len 
n = int(input())
a = list(map(int,input().split()))
print(maxlen(a,n))

'''

Jack is fond of numbers. He has given an array.He has to find the maximum length of sub array such that sum of elements in that sub array gives output 0.He is in little trouble, help him in finding solution

Input Description:
You are given an integer ‘n’ denoting the number of elements in array.Next line contains n space separated integers

Output Description:
Print the max length of that array with sum 0 and print -1 if not possible

Sample Input :
6
-4 3 1 0 0 6

Sample Output :
5

'''
