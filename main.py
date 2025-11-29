# 1
kop = lambda x: x * 5
print(kop(7))

# 2
kop = lambda a, b: a * b
print(kop(4, 6))

# 3
juft_toq = lambda x: "juft" if x % 2 == 0 else "toq"
print(juft_toq(7))
print(juft_toq(10))

# 4
katta = lambda a, b: a if a > b else b
print(katta(10, 7))
print(katta(3, 15))

# 5
uzunlik = lambda name: True if len(name) > 7 else False
uzunlik = lambda name: len(name) > 7

print(uzunlik("Abdulloh"))
print(uzunlik("Ali"))
