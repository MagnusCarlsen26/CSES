def find(x: int, y: int) -> int:
    minOrderSquare = max(x, y)

    startNumber = minOrderSquare**2
    if minOrderSquare%2 == 0:
        # Start at botom left of minOrder Square and go towards right decreasing the {number}??
        backwardSteps = (minOrderSquare - y) + (x-1)
    else:
        # Start at top right of minOrder Square and go downwards decreasing the {number}??
        backwardSteps = (minOrderSquare - x) + (y-1)
    
    numberAtXY = startNumber - backwardSteps
    return numberAtXY

def main():

    for _ in range(int(input())):
        y, x = map(int,input().split())
        print(find(x,y))

main()