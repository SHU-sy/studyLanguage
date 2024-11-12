import base64
import sys
s = sys.stdin.readline().strip()
date = s.encode('utf-8')
encoded = base64.b32encode(date)
print(encoded.decode('utf-8'))