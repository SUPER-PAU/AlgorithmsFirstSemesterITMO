def matches(template, string):
    n, m = len(template), len(string)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        if template[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
        else:
            break
    print(dp[0])
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if template[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif template[i - 1] == '?' or template[i - 1] == string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
        print(dp[i])

    return dp[n][m]

def main():
    with open("input.txt") as file:
        template = file.readline().strip()
        string = file.readline().strip()

    if matches(template, string):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()