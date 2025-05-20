import sys
import bisect
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    dp = []

    for i in arr:
        index = bisect.bisect_left(dp, i)
        if index == len(dp):
            dp.append(i)
        else:
            dp[index] = i
    print(len(dp))


if __name__ == "__main__":
    sys.exit(main())