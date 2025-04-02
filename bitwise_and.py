'''
Created on Apr 2, 2025

@author: bigcv
'''
#!/bin/python3

def bitwiseAnd(N, K):
    if K % 2 == 1:
        return K - 1
    elif N >= K | (K - 1):
        return K - 1
    else:
        return K - 2

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        
        res = bitwiseAnd(count, lim)
        print(str(res) + '\n')
