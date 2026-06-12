# 1084. Apartments

def main():
    n, m, k = map(int, input().split())
    desiredSize = list(map(int, input().split()))
    apartmentsSizeAvailable = list(map(int,input().split()))

    desiredSize.sort()
    apartmentsSizeAvailable.sort()

    numOfApartmentsGranted = 0
    startingApartmentIndexAvailable = 0
    for i in range(n):
        
        while startingApartmentIndexAvailable < m and apartmentsSizeAvailable[startingApartmentIndexAvailable] < desiredSize[i] - k:
            startingApartmentIndexAvailable += 1

        if startingApartmentIndexAvailable >= m:
            break

        if apartmentsSizeAvailable[startingApartmentIndexAvailable] >= desiredSize[i] - k:
            if apartmentsSizeAvailable[startingApartmentIndexAvailable] <= desiredSize[i] + k:
                startingApartmentIndexAvailable += 1
                numOfApartmentsGranted += 1
            else: continue

    print(numOfApartmentsGranted)

main()