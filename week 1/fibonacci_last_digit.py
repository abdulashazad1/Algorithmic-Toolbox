def fibonacci_last_digit(n):
    #compute the fibonnaci num first
    number = fibonacci_number(n)
    return int(str(number)[-1])
    
def fibonacci_number(n):
    list = [0, 1]
    for i in range(2, n+1):
        list.append((list[i-1] +list[i-2])%10)
    return list[n]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
