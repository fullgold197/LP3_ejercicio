#Ejercicio que determine si un estudiante esta aprobado o no
#Autor: Oscar Vilca Rivera

def determinaraprobado(promedio):
    if promedio>=11:
        resultado="Aprobado"
    else:
        resultado="Desaprobado"
    return resultado

promedio=int(input(f"El promedio es: "))
print(determinaraprobado(promedio))
