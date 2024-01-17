
def change(money):
    # write your code here

    #denominatios are 1,3, and 4. Find min number of coins to changee money

    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (money + 1)
    
    # Base case: 0 coins needed to make change for 0
    dp[0] = 0
    
    # Define the coin denominations
    denominations = [1, 3, 4]

    # Dynamic programming approach to find the minimum number of coins
    for i in range(1, money + 1):
        for coin in denominations:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
