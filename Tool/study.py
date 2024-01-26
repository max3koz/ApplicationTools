import math

"""
Open and read file

with open('study.py', mode='r+') as file:
    data = file.read()
    file.seek(0, 2)
    file.write('print(data)\n')
"""

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
"""

q_ty_caps = int(input("Enter coffee caps q-ty: "))

q_ty_bonus_cap = q_ty_caps//7
print(q_ty_bonus_cap)

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dist = round(math.sqrt((x2-x1)**2 + (y2-y1)**2),3)
print(dist)

chicken = int(input("Enter q-ty of the chicken: "))
cow = int(input("Enter q-ty of the cow: "))
pig = int(input("Enter q-ty of the pig: "))

legs = chicken * 2 + (cow + pig) * 4
print(legs)

