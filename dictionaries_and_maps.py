'''
Created on Mar 21, 2025

@author: bigcv
'''
import sys

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    phonebook = {}
    for i in range(1, int(lines[0]) + 1):
        entry = lines[i].split()
        phonebook.update({entry[0]: entry[1]})
        
    for i in range(int(lines[0]) + 1, len(lines)):
        num = phonebook.get(lines[i])
        if num is None:
            print("Not found")
        else:
            print(f"{lines[i]}={num}")
