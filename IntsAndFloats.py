from decimal import Decimal, getcontext


print(10/3)

print(int(4 ** 4.0))
print(int(4.0)) #casting to int produces the trucnation of decimal section
print(4.0)


print(round(14/3, 2))
print(int('100', 2))

print(getcontext())
getcontext().prec = 4
print(getcontext())



print(Decimal(1.2)/Decimal(1.0))