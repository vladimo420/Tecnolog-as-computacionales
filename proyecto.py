"""
Programa: Evaluación de calificaciones (versión final con API externa)
Autor: [Tu nombre]
Descripción:
Permite registrar nombres y calificaciones de estudiantes,
calcula promedio, aprobados y reprobados usando una API externa (statistics).
"""

import statistics  


# ================= FUNCIONES =================


def calcular_promedio(lista_estudiantes):
    """
    Calcula el promedio general usando statistics.mean().
    Parámetros:
        lista_estudiantes (list): lista anidada con [nombre, calificación]
    Retorna:
        float: promedio general
    """
    if not lista_estudiantes:
        return 0.0

    # Extrae solo las calificaciones (posición [1] de cada sublista)
    calificaciones = [estudiante[1] for estudiante in lista_estudiantes]

    promedio = statistics.mean(calificaciones)  
    return promedio


def contar_aprobados(lista_estudiantes, minimo_aprobacion):
    """
    Cuenta cuántos estudiantes aprobaron según el mínimo de aprobación.
    Parámetros:
        lista_estudiantes (list): lista anidada con [nombre, calificación]
        minimo_aprobacion (float): nota mínima para aprobar
    Retorna:
        int: número de aprobados
    """
    aprobados = 0
    for estudiante in lista_estudiantes:
        if estudiante[1] >= minimo_aprobacion:
            aprobados += 1
    return aprobados


def generar_reporte(lista_estudiantes, minimo_aprobacion):
    """
    Genera un reporte general del grupo.
    Parámetros:
        lista_estudiantes (list): lista anidada con [nombre, calificación]
        minimo_aprobacion (float): nota mínima para aprobar
    Retorna:
        dict: contiene promedio, aprobados, reprobados
    """
    promedio = calcular_promedio(lista_estudiantes)
    aprobados = contar_aprobados(lista_estudiantes, minimo_aprobacion)
    reprobados = len(lista_estudiantes) - aprobados

    return {
        "promedio": round(promedio, 2),
        "aprobados": aprobados,
        "reprobados": reprobados
    }


# ================= PROGRAMA PRINCIPAL =================


def main():
    """
    Función principal del programa.
    """
    num_estudiantes = int(input("Ingrese el número de estudiantes: "))
    estudiantes = []

    for i in range(num_estudiantes):
        nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
        calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
        estudiantes.append([nombre, calificacion])  # lista anidada

    minimo_aprobacion = float(input("Ingrese la calificación mínima para aprobar: "))

    reporte = generar_reporte(estudiantes, minimo_aprobacion)

    print("\n--- REPORTE FINAL ---")
    print(f"Promedio general: {reporte['promedio']}")
    print(f"Estudiantes aprobados: {reporte['aprobados']}")
    print(f"Estudiantes reprobados: {reporte['reprobados']}")


# Punto de entrada
if __name__ == "__main__":
    main()