n = int(input())

if n == 1:
    print(1)
    exit()
if n<=3 :
    print("NO SOLUTION")
    exit()
if n == 4:
    print("2 4 1 3")
    exit()
for i in range(1, n+1, 2):
    print(i, end=" ")
for i in range(2, n+1, 2):
    print(i, end= " ")