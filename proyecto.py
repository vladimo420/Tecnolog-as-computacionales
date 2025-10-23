
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




# Avance 4:
# Uso de estructuras condicionales (if / else)

def contar_aprobados(lista_estudiantes, minimo_aprobacion):
    """
    Cuenta cuántos estudiantes aprobaron según el mínimo de aprobación.
    """
    aprobados = 0
    for estudiante in lista_estudiantes:
        if estudiante[1] >= minimo_aprobacion:
            aprobados += 1
    return aprobados


# Avance 5:
# Uso de estructuras cíclicas (for)


def generar_reporte(lista_estudiantes, minimo_aprobacion):
    """
    Genera un reporte general del grupo.
    """
    promedio = calcular_promedio(lista_estudiantes)
    aprobados = contar_aprobados(lista_estudiantes, minimo_aprobacion)
    reprobados = len(lista_estudiantes) - aprobados

    return {
        "promedio": round(promedio, 2),
        "aprobados": aprobados,
        "reprobados": reprobados
    }
