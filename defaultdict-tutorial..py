# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = input().split(" ")

a = [input() for _ in range(int(n))]

b = [input() for _ in range(int(m))]

dic = defaultdict(lambda: [])


for i, v in enumerate(a, start=1):
    dic[v].append(i)

for v in b:
    if not dic[v]:
        print(-1)
    else:
        print(*dic[v]) 
