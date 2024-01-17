def compute_operations(n):
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(1, n + 1):
        if i + 1 <= n:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        if 2 * i <= n:
            dp[2 * i] = min(dp[2 * i], dp[i] + 1)
        if 3 * i <= n:
            dp[3 * i] = min(dp[3 * i], dp[i] + 1)

    # Construct the output sequence
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 3 == 0 and dp[n // 3] == dp[n] - 1:
            n //= 3
        elif n % 2 == 0 and dp[n // 2] == dp[n] - 1:
            n //= 2
        else:
            n -= 1
    sequence.append(1)

    return sequence[::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
