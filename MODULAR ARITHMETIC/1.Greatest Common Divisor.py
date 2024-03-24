def gcd(a,b): #유클리드 호재법을 이용한 최대공약수 구하기
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(66528, 52920))