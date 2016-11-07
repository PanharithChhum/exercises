#Given numbers 1 2 3 4 5 6 7 8 9 and only the operations +, -, and concatenate
#How different ways are there to make 100
#e.g. 1+2+3-4+5+6+78+9
#Optimized for efficiency using a generator

from itertools import zip_longest, product

def check(string):
    string = string.replace('c','')
    return eval(string)

def merge(*iterators):
    '''merge iterators, ignoring Nones
    '''
    for items in zip_longest(*iterators):
        yield from filter(None, items)

def combo(target, limit=9, start=1):

    numbers = list(map(str, range(start, limit + 1)))
    operations = ['+','-','c']

    for ops in product(operations, repeat=len(numbers)-1):
        expression = ''.join(merge(numbers, ops))

        if check(expression) == target:
            yield expression

def main():
    for sol in combo(100, limit = 9):
        print(sol)

main()