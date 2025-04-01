'''
Created on Mar 21, 2025

@author: bigcv
'''


if __name__ == "__main__":
    n = int(input().strip())
    nbin = bin(n)
    count = 0
    max_count = 0
    for i in nbin:
        if i == "1":
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)
    
    
    