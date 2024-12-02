a, b, c, m = map(int, input().split())
p = 0
w = 0

if a<=m:
	for _ in range(24):
		if a+p > m:
			p -= c
			if p < 0:
				p = 0

		else:
			w += b
			p += a

print(w)