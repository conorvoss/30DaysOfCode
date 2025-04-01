'''
Created on Mar 27, 2025

@author: bigcv
'''

class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        d = [n]
        for x in range(1, n // 2 + 1):
            if n % x == 0:
                d.append(x)
                
        return sum(d)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)