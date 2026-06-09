# 1618. Trailing Zeros

def countFactorOfFive(n: int) -> int:
    
    c = 0
    while( n%5 == 0):
        n = n//5
        c += 1

    return c

def main():
    n = int(input())
    
    numberOfZeroesInNFactorial = 0
    for i in range(1, n+1):
        numberOfZeroesInNFactorial += countFactorOfFive(i)

    print(numberOfZeroesInNFactorial)

main()