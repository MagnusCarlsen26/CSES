def computeXOR(a: int, b: int) -> int:
    return a ^ b


def computeXNOR(a: int, b: int) -> int:
    return ~computeXOR(a, b)


def findMissingNumber(n: int, lst: list) -> int:

    XORofEntireSeries = 1
    for i in range(2, n + 1):
        XORofEntireSeries = computeXNOR(XORofEntireSeries, i)

    XORofGivenSeries = lst[0]
    for index in range(1, n - 1):
        XORofGivenSeries = computeXNOR(XORofGivenSeries, lst[index])

    missingNumber = computeXNOR(XORofGivenSeries, XORofEntireSeries)

    return missingNumber


def main():
    n = int(input())
    lst = list(map(int, input().split()))

    print(findMissingNumber(n, lst))


main()

# Analysis
# - Time - O(n)
#   Space - O(1) additional
