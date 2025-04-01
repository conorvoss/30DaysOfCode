'''
Created on Mar 21, 2025

@author: bigcv
'''


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(" ".join([str(arr[i]) for i in range(len(arr) - 1, -1, -1)]))
