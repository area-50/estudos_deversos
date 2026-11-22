from random import randint
from time import time


MAX_NUMBER = 999999
MIN_NUMBER = 0

random_numbers = [
    randint(MIN_NUMBER, MAX_NUMBER) for i in range(MAX_NUMBER + 1)
]

def timer(func):
    def inner(args):
        start = time()
        func(args)
        finish = time()
        print(f'O programa levou {round(finish - start, 2)}s')
    return inner

@timer
def insertion_sort(array: list):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i -1

        array[i + 1] = key


if __name__ == '__main__':
    
    insertion_sort(random_numbers)
    input('Aperte enter para continuar!')
    print(random_numbers)