'''
Created on Apr 1, 2025

@author: bigcv
'''
from math import sqrt

def is_prime(n):
    if n < 2:
        return "Not prime"
    
    sq = int(sqrt(n))
    for x in range(2, sq + 1):
        if n % x == 0:
            return "Not prime"
    return "Prime"

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        print(is_prime(int(input().strip())))
