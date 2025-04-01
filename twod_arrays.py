'''
Created on Mar 21, 2025

@author: bigcv
'''

def calc_hg(arr, x, y, hg_dim):
    hg_mid = hg_dim / 2
    row_start = y
    row_end = y + hg_dim
    col_start = x
    col_end = x + hg_dim
    total = 0
    row = 1
    
    for i in range(row_start, row_end):
        total += sum(arr[i][col_start:col_end])
        if row < hg_mid:
            col_start += 1
            col_end -= 1
        elif row > hg_mid:
            col_start -= 1
            col_end += 1
        row += 1
    
    return total


if __name__ == '__main__':

    arr = []
    hg_dim = 3

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    hg_per_col = len(arr) - hg_dim + 1
    hg_per_row = len(arr[0]) - hg_dim + 1
    hgs = [calc_hg(arr, x, y, hg_dim) for x in range(hg_per_row) for y in range(hg_per_col)]

    print(arr)
    print(hgs)
    print(len(hgs))
    print(max(hgs))
        

