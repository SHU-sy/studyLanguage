A, B, C = [int(input().strip()) for _ in range(3)]
result = A * B * C
result_str = str(result)
count_digits = [0] * 10

for digit in result_str:
    count_digits[int(digit)] += 1

for count in count_digits:
    print(count)