import sys
import bisect
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    lines = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    arr = []
    lis = []

    arr = [b for _, b in lines]

    for i in arr:
        index = bisect.bisect_left(lis, i)
        if index == len(lis):
            lis.append(i)
        else:
            lis[index] = i
    print(n - len(lis))


if __name__ == "__main__":
    sys.exit(main())