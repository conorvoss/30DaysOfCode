'''
Created on Apr 2, 2025

@author: bigcv
'''
#!/bin/python3

if __name__ == '__main__':
    N = int(input().strip())
    names = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        if emailID[-10:] == "@gmail.com":
            names.append(firstName)
    
    names.sort()
    print("\n".join(names))
