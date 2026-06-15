# 1640. Sum of Two Values
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
lst = list(map(int, input().split()))

d = {}
s = set()
for i in range(n):
    if lst[i] not in s:
        s.add(lst[i])
        d[lst[i]] = [i]
    else:
        if len(d[lst[i]]) > 2:
            continue
        d[lst[i]].append(i)

for i in lst:
    if x - i in d:
        if x-i != i:
            print(d[i][0] + 1, d[x-i][0] + 1)
            break
        elif x-i == i:
            if len(d[i]) != 1:
                print(d[i][0] + 1, d[i][1] + 1)
                break
        else:
            exit()
else:
    print("IMPOSSIBLE")