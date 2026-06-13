# 1619. Restaurant Customers

def createMapper(customerInOutTimes: list) -> dict:

    d = {}

    c = 0

    l = []
    for i in customerInOutTimes:
        l.append(i[0])
        l.append(i[1])

    l.sort()

    for i in l:
        if i not in d:
            d[i] = c
            c += 1

    return d


def maxConcurrentCustomerCount(n: int, customerInOutTimes: list) -> int:

    spaceMapper = createMapper(customerInOutTimes)

    concurrentHeatMap = [0]*(len(spaceMapper)+1)
    for i in customerInOutTimes:
        concurrentHeatMap[spaceMapper[i[0]]] = 1
        concurrentHeatMap[spaceMapper[i[1]]] = -1

    max = 0
    c = 0
    for i in concurrentHeatMap:
        c += i
        if max<c:
            max = c

    return max

def main():
    n = int(input())
    customerInOutTimes = []
    for _ in range(n):
        customerInTime, customerOutTime = map(int, input().split())
        customerInOutTimes.append((
            customerInTime,
            customerOutTime
        ))

    print(maxConcurrentCustomerCount(n, customerInOutTimes))    

main()