# 입력
a, b, c = map(int, (input().split()))

# 출력
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a%c)*(b%c))%c)