cipher=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(0, 256): # 1바이트 범위로 브루트 포스
    search="".join(chr(c^i) for c in cipher) # 문자열 저장
    if('crypto' in search):
        print(search)