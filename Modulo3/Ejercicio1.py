calificacion = float(input("Calificación: "))

if calificacion >= 6 and calificacion < 9:
    print("Aprobado")
    
if calificacion < 6 and calificacion >= 0:
    print("Reprobado")

if calificacion >= 9 and calificacion <= 10:
    print("Excelente")

if calificacion < 0 or calificacion > 10:
    print("Calificación inválida")

if calificacion < 9 and calificacion > 8:
    print("Buen trabajo")
    
'''a) Si la calificación es 9 o más, diga «Excelente».
b) Si es menor que 0 o mayor que 10, diga «Calificación inválida».
c) si la calificación es mayor que 8 pero menor que 9 que diga buen trabajo'''
