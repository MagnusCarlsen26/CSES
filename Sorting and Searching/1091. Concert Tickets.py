# 1091. Concert Tickets

n, m = map(int, input().split())
concertPrices = list(map(int, input().split()))
customerBidPrices = list(map(int, input().split()))

concertPrices.sort()
customerBidPrices.sort(reverse=True)

concertPricesLastAvailableIndex = n-1

for bidPrice in range(m):
    
    if concertPricesLastAvailableIndex < 0:
        print(-1)
        continue

    start, end = 0, concertPricesLastAvailableIndex
    ans = -1
    while(start < end):
        mid = start + (end - start)//2
        if concertPrices[mid] == customerBidPrices[bidPrice]: 
            print(concertPrices[mid])
            break
        elif concertPrices[mid] > customerBidPrices[bidPrice]:
            concertPricesLastAvailableIndex = mid - 1
            end = mid - 1
        elif concertPrices[mid] < customerBidPrices[bidPrice]:
            ans = concertPrices[mid]
            start = mid + 1
        else:
            exit()
    
    print(ans)
