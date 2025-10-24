"""
Proyecto Final Python
Control y registro de calificaciones
Autor: [Vladimir Mondragon Galan]

Descripción general:
Este programa permite registrar nombres y calificaciones de estudiantes,
calcular el promedio del grupo, y determinar cuántos aprobaron o reprobaron.
Además, utiliza la API externa 'statistics' del módulo estándar de Python
para calcular el promedio de manera eficiente.


"""

# =====================  BIBLIOTECAS  ==========================================
import statistics  # API externa: módulo estándar de Python (https://docs.python.org/3/library/statistics.html)

# ==============================================================================
#                       FUNCIONES PRINCIPALES
# ==============================================================================


def calcular_promedio(lista_estudiantes):
    """
    (uso de funciones, listas anidadas, API externa)
    recibe: lista_estudiantes (lista anidada con pares [nombre, calificación])
    proceso: extrae las calificaciones y calcula su promedio
             usando statistics.mean()
    devuelve: promedio (float)
    """
    if not lista_estudiantes:
        return 0.0

    calificaciones = [estudiante[1] for estudiante in lista_estudiantes]
    promedio = statistics.mean(calificaciones)  # Uso de API externa
    return promedio


def contar_aprobados(lista_estudiantes, minimo_aprobacion):
    """
    (uso de condicionales, ciclos y operadores)
    recibe: lista_estudiantes (lista anidada con pares [nombre, calificación]),
            minimo_aprobacion (float)
    proceso: cuenta cuántos estudiantes tienen calificación >= mínimo
    devuelve: número entero de aprobados
    """
    aprobados = 0
    for estudiante in lista_estudiantes:
        if estudiante[1] >= minimo_aprobacion:
            aprobados += 1
    return aprobados


def generar_reporte(lista_estudiantes, minimo_aprobacion):
    """
    (uso de funciones, diccionarios, ciclos y operadores)
    recibe: lista_estudiantes (lista anidada con pares [nombre, calificación]),
            minimo_aprobacion (float)
    proceso: calcula promedio, número de aprobados y reprobados
    devuelve: diccionario con promedio, aprobados y reprobados
    """
    promedio = calcular_promedio(lista_estudiantes)
    aprobados = contar_aprobados(lista_estudiantes, minimo_aprobacion)
    reprobados = len(lista_estudiantes) - aprobados

    reporte = {
        "promedio": round(promedio, 2),
        "aprobados": aprobados,
        "reprobados": reprobados
    }
    return reporte


# ==============================================================================
#                       FUNCIONES AUXILIARES
# ==============================================================================


def registrar_estudiantes(num_estudiantes):
    """
    (uso de ciclos, listas anidadas y operadores)
    recibe: num_estudiantes (int)
    proceso: solicita al usuario nombre y calificación de cada estudiante
    devuelve: lista anidada con pares [nombre, calificación]
    """
    estudiantes = []
    print("\n--- Registro de Estudiantes ---")
    for i in range(num_estudiantes):
        print(f"\nEstudiante {i + 1} de {num_estudiantes}:")
        nombre = input(" → Nombre: ").strip().title()
        calificacion = float(input(f" → Calificación de {nombre}: "))
        estudiantes.append([nombre, calificacion])
    return estudiantes


def mostrar_reporte(reporte):
    """
    (uso de funciones y salida formateada)
    recibe: reporte (diccionario)
    muestra en pantalla los resultados de manera amigable
    """
    print("\n================== REPORTE FINAL ==================")
    print(f"Promedio general del grupo: {reporte['promedio']}")
    print(f"Total de estudiantes aprobados: {reporte['aprobados']}")
    print(f"Total de estudiantes reprobados: {reporte['reprobados']}")
    print("===================================================")


# ==============================================================================
#                       PARTE PRINCIPAL DEL PROGRAMA
# ==============================================================================


def main():
    """
    Función principal del programa.
    Integra todas las funciones anteriores para formar un flujo completo.
    """
    print("===============================================")
    print("     Bienvenido al simulador de calificaciones  ")
    print("===============================================")
    print("             Instrucciones de uso             ")
    print(" Ingresa valores númericos mayores o iguales  0")


    num_estudiantes = int(input("\nIngrese el número total de estudiantes: "))

    # Registro de estudiantes (lista anidada)
    lista_estudiantes = registrar_estudiantes(num_estudiantes)

    # Ingreso del criterio de aprobación
    minimo_aprobacion = float(input("\nIngrese la calificación mínima para aprobar: "))

    # Procesamiento de datos
    reporte = generar_reporte(lista_estudiantes, minimo_aprobacion)

    # Presentación de resultados
    mostrar_reporte(reporte)

    print("\nGracias por usar el simulador de calificaciones.")
    print("¡Hasta la próxima!")


# ==============================================================================
#                            PUNTO DE ENTRADA
# ==============================================================================
if __name__ == "__main__":
    main()
