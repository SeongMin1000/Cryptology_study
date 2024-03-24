def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean(b, a % b)
        return gcd, y, x - (a // b) * y

# 앞서 진행한 유클리드 호재법에서 GCD(a,b)=GCD(b,a%b)인 것을 알았으므로
# ax+by=gcd와 bx+(a%b)y=gcd 같음을 보인다
# (a%b)=a-(a//b)b 이므로
# gcd=bx+(a-(a//b)b)y=ay+b(x-y(a//b))로 표현된다
    
a = 26513
b = 32321
gcd, x, y = extended_euclidean(a, b)
print(f"GCD({a}, {b}) = {gcd}")
print(f"{a}*{x} + {b}*{y} = {gcd}")