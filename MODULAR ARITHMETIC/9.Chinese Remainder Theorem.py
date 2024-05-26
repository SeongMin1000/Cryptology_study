def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_gcd(b, a%b)
        return (gcd, y, x - (a // b) * y)

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd == 1 :
        return x % m

def chinese_remainder_theorem(n, a):
    prod = 1
    for i in n:
        prod *= i

    result = 0
    for i in range(len(n)):
        ni = prod // n[i]
        result += a[i] * mod_inverse(ni, n[i]) * ni

    return result % prod

n = [5, 11, 17]  # 모듈러 값들
a = [2, 3, 5]  # 각 모듈러 값들에 대한 나머지
print(chinese_remainder_theorem(n, a))

# 중국 나머지 정리
    # x = a mod n1
    # x = b mod n2
    # x = c mod n3
    # .... 와 같이 있을 때 N = n1*n2*n3*...을 구한 후
    # N//n1 , N//n2, N//n3 값들을 구하고 이 값들의 역원을 구한다
    # 역원 값들을 각각 N//n1, N//n2, N//n3 ...에 곱하고 나머지 a,b,c와 곱한 다음
    # 이들의 합을 다시 N으로 나눈다
