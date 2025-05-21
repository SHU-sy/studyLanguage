def solution(m, n, puddles):
    MOD = 1000000007

    # 2차원 배열 초기화 (1-indexed)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작점

    # 물에 잠긴 곳 표시 (y, x 순서 주의)
    puddle_set = set((y, x) for x, y in puddles)

    # 그래프처럼 순차적으로 dp 채우기
    for i in range(1, n + 1):      # 행
        for j in range(1, m + 1):  # 열
            if (i, j) in puddle_set or (i == 1 and j == 1):
                continue  # 물에 잠기거나 시작점은 건너뜀
            # 위(i-1, j)와 왼쪽(i, j-1)에서 오는 경로 수를 더함
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[n][m]
