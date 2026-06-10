def isSeriesSumEven(n: int):

    if n%2 == 0:
        if (n+1)%2 == 0:
            return True
        elif n%4 == 0:
            return True
        return False
    else:
        if (n+1)%4 == 0:
            return True
        return False

def printInOppisitePairs(start: int, end: int, parity: bool):

    for i in range(start, start + (end-start)//2 + 1):
        if i%2 == parity:
            print(i, end=" ")
            print((start+end)-i, end= " ")
def solve(n: int):

    if not isSeriesSumEven(n):
        print("NO")
        return
    
    print("YES")
    
    if n%2 == 0:
        print(n//2)
        printInOppisitePairs(1,n, True)
        print(n//2)
        printInOppisitePairs(1,n, False)
    else:
        print((n+1)//2)
        print("1", end=" ")
        print("2", end=" ")
        printInOppisitePairs(4,n,False)
        print()
        print((n-1)//2)
        print("3", end=" ")
        printInOppisitePairs(4, n, True)

def main():
    n = int(input())
    solve(n)

main()