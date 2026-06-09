n = int(input())

if n<1 :
    print(f"ABORT: Expected n >=1 but received {n}")
    exit()

while n != 1:
    # Expensive operation because integer is converted to a string and then a syscall to kernel
    # is made which is expensive. Typically syscall isn't made every time. It maintains a buffer
    # and flushes the buffer periodically. Otherwise it would be even more expensive.
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

print(1)

# Analysis
# - Time O(k) -> K is sequence length of collatz conjecture.
#   Space O(1)
# - Validate value of n before processing.
# 1. Integer can overflow when computing 3*n + 1.
# - Python allows arbitarily large values. You can declare an integer `x = 10*1000` and python 
#   handle it. Because integer is an object in python. x = 1 will take roughly 28 bytes of space
#   because of object memory overhead.
# - In Java, integer can both be an primitve and object. if you declare `int x = 1` then its a 
#   primitive and will only take 4 bytes. 8 bytes in case of `long`. but if Integer is used then
#   Java considers that an object and it will take ~16 bytes. Integer still has limit of 4 bytes.
#   Use Java BigInteger for arbitary precision.
# - In C++ it is always an integer. Always taking 4 bytes.
#   Computation in case of primitive data types are obviously faster because CPUs have direct hardware
#   support. Computation in python is slower but more convinient when dealing with large numbers.
# 2. This is collatz conjecture. We don't have any proof whether this loop will ever break or not.
#   Good to have a max limit on number of iterations

# ChatGPT Discussion
# https://chatgpt.com/share/6a278863-6da8-83e8-9950-93b796e741d2