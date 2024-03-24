import base64

HexString="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
ByteString=bytes.fromhex(HexString) # 16진수 문자열을 바이트 문자열로 변환
print(base64.b64encode(ByteString)) # 바이트 문자열을 다시 base64 형태 문자열로 인코드