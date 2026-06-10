# 1754. Coin Piles
# https://chatgpt.com/share/6a28f907-4cc0-83e8-a918-272ac9154b1f
import math

def solve(a: int, b: int) -> bool:

    # Original solution was that (4b-2a)/3 should be an integer. By clever optimizations.
    # Also 4b-2a >= 0
    # This is the most optimal solution. 
    if (a%3 + b%3)%3 == 0:
        if a >= math.ceil(b/2) and b >= math.ceil(a/2):
            return True
    return False

def main():
     
    for _ in range(int(input())):
        a, b = map(int, input().split())

        print("YES") if solve(a, b) else print("NO")

main()