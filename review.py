'''
Created on Mar 21, 2025

@author: bigcv
'''
import sys
def split(word):
    evens = "".join([word[x] for x in range(len(word)) if x % 2 == 0])
    odds = "".join([word[x] for x in range(len(word)) if x % 2 == 1])
    print(evens, odds)


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    for i in range(1, len(lines)):
        split(lines[i].strip())