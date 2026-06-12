# 1621. Distinct Numbers

def solve(n: int, lst: list) -> int:
    return len(set(lst))
def main():
    n = int(input())
    lst = list(map(int,input().split()))
    print(solve(n, lst))

main()

# Analysis
# https://codeforces.com/blog/entry/122914
# Why the fuck same problem when solved using dict takes 3s+ to run. TLE 
# For memory constraint issues sort the array. Space O(logn) Time O(nlogn)
# For spare 