def recursive_simple_multiplier(number : float, factor: int, count: int) -> float:
    if count == 0:
        return number

    count -= 1

    return recursive_simple_multiplier(number*factor, factor, count)



if __name__ == '__main__':
    print(recursive_simple_multiplier(3, 4, 2))