"""
Open and read file


with open('study.py', mode='r+') as file:
    data = file.read()
    file.seek(0, 2)
    file.write('print(data)\n')
"""

import sys
print(sys.getdefaultencoding())
print(ord('a'))
print(ord("A"))
print(chr(1023))
s = "Hello"
enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8')
enc_utf16 = s.encode('utf16')

print(type(enc_ascii))
print(enc_ascii)
print(enc_utf8)
print(enc_utf16)

print(len(enc_ascii))
print(len(enc_utf8))
print(len(enc_utf16))
