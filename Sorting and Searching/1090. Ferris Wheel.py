# 1090. Ferris Wheel
n, x = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

gondalasUsed = 0
left, right = 0, n-1
while(left<right):
    if lst[left] + lst[right] <=x:
        left += 1
        right -= 1
    else:
        right -= 1
    gondalasUsed += 1
        

print(gondalasUsed + int(left == right))