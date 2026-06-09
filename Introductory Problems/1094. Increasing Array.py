def findMinOperationsForIncreasingArray(lst: list) -> int:

    numberOfOperationsForIncreasingArray = 0
    previousElement = lst[0]
    for index in range(1, len(lst)):
        if lst[index] < previousElement:
            numberOfOperationsForIncreasingArray += previousElement - lst[index]
        else:
            previousElement = lst[index]

    return numberOfOperationsForIncreasingArray


def main():

    n = int(input())
    lst = list(map(int, input().split()))

    print(findMinOperationsForIncreasingArray(lst))


main()
