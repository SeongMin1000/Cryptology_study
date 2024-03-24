from pwn import *

cipher=b'label'
print(xor(cipher,13)) # label과 13을 xor
