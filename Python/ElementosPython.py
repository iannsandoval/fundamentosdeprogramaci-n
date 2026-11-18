nombre = "Ana" #variable de tipo string
edad = 19 #variable de tipo entero
estatura = 1.65 #variable de tipo flotante
es_estudiante = True #variable de tipo booleano

print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("Estudiante:", es_estudiante, type(es_estudiante))

PROMEDIO_MINIMO = 6

materia = input("Que materia cursas? ")
calificación =float(input("¿Que materia cursas? "))

suma = 0 + 2 
resto = 10 % 3
potencia = 2 ** 3
mayor_de_edad = edad >= 18
aprobado = calificación >= PROMEDIO_MINIMO and es_estudiante

print("suma:", suma,  "| Resto:", resto, "| Potencia:", potencia)
print("¿Mayor de edad?", mayor_de_edad)