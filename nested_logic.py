'''
Created on Apr 1, 2025

@author: bigcv
'''

if __name__ == "__main__":
    ret = list(map(int, input().strip().split()))
    due = list(map(int, input().strip().split()))
    if ret[2] > due[2]:
        fine = 10000
    elif ret[2] == due[2] and ret[1] > due[1]:
        fine = 500 * (ret[1] - due[1])
    elif ret[2] == due[2] and ret[1] == due[1] and ret[0] > due[0]:
        fine = 15 * (ret[0] - due[0])
    else:
        fine = 0
    
    print(fine)