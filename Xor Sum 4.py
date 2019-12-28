import numpy as np

MAX_DIGIT = 60
MOD = 10 ** 9 + 7

N = int(input())
A = np.array([int(a) for a in input().split()])
B = [int(a) for a in input().split()]
print(A)
print(B)
answer = 0
for d in range(MAX_DIGIT + 1):
    A, r = (A >> 1), A % 2
    s = int(r.sum())
    base = (1 << d) % MOD
    answer += (base * s * (N - s)) % MOD
    print(answer)

answer %= MOD
print(answer)
