from itertools import permutations

def max_dot_product(a, b):
    res = 0
    for i in range(len(a)):
        max_a = get_max_index(a)
        max_b = get_max_index(b)
        res = res + a[max_a] * b[max_b]
        del a[max_a]
        del b[max_b]
    return res

def get_max_index(array):
    max = array[0]
    index = 0
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
            index = i
    return index


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
