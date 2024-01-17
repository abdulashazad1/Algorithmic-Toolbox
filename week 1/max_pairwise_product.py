def max_pairwise_product(numbers):
    max1 = 0
    max2 = 0
    max1Index = 0
    for i in range(len(numbers)):
        if numbers[i] >= max1:
            max1 = numbers[i]
            max1Index = i
    for j in range(len(numbers)):
        if numbers[j] >= max2 and j!=max1Index:
            max2 = numbers[j]
    return max1*max2
        

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
