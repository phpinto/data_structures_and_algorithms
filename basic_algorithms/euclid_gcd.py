def gcd(a, b):
    rem = a % b
    while(rem != 0):
        a = b
        b = rem
        rem = a%b
    return b

print(gcd(20,8))
print(gcd(36,14))
print(gcd(99,11))
print(gcd(173,57))