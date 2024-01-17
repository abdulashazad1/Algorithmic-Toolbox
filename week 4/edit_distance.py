def edit_distance(S, T):
    n = len(S)
    m = len(T)

    dp = [[0 for x in range(m + 1)] for x in range(n + 1)]
    

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i][j-1], #insert
                                    dp[i-1][j],  #delete
                                    dp[i-1][j-1])   #replace
    return dp[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
