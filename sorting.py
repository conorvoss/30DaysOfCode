'''
Created on Mar 27, 2025

@author: bigcv
'''
#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    
    sort = False
    total_swaps = 0
    while not sort:
        swaps = 0
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                swaps += 1
        total_swaps += swaps
        if swaps == 0:
            sort = True
    
    print(f"Array is sorted in {total_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
