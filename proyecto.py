
# Avance 2:
# Uso de operadores aritméticos

# En este avance se usarán operaciones matemáticas simples
# para calcular el promedio de calificaciones.

# Avance 3:
# Separación de código en funciones reutilizables.

def calcular_promedio(lista_estudiantes):
    """
    Calcula el promedio general de las calificaciones.
    """
    if not lista_estudiantes:
        return 0.0

    suma = 0
    for estudiante in lista_estudiantes:
        suma += estudiante[1]  # operador aritmético
    promedio = suma / len(lista_estudiantes)
    return promedio
