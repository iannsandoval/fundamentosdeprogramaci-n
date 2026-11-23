import math

radio = float(input("Radio del círculo: "))

area = math.pi * math.pow(radio, 2)
perimetro = 2 * math.pi * radio

print("Area:", round(area, 2))
print("Perimetro:", round(perimetro, 2))
print("Raíz cuadrada del radio:", round(math.sqrt(radio), 2))
print("Techo del área:", math.ceil(area))

x = 4
y = 3
pow = math.pow(x, y)
print("x =", x, ", y =", y)
print("x^y =", pow)

z= 100
log= math.log10(z)
print("log10(", z, ") =", log)
