print("información sobre concepto de suma")

# ejercicio

def suma(a, b):
    # La función ahora verifica si los valores de entrada son números
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Si son números, devuelve el resultado de la suma
        return a + b
    else:
        # Si no son números, devuelve un mensaje de error
        return "Error: Ambos valores deben ser números para realizar la suma."

print("realiza la suma de 5+13")
print("escribe el resultado de tu suma")
# Se asume que la entrada del usuario será un número, como en el código original.
resultado_suma = int(input())

# La variable 'resultado_funcion' guarda el valor devuelto por la función
resultado_funcion = suma(5, 13)

# La condición ahora verifica si el resultado de la función es un número antes de compararlo
if isinstance(resultado_funcion, (int, float)):
    if resultado_funcion == resultado_suma:
        print("Muy bien, la respuesta es =", resultado_funcion, ". Gran trabajo, sigue asi")
    else:
        print("tu respuesta es incorrecta, sigue practicando :(")
else:
    # Si la función devolvió un error (no es un número), se imprime el mensaje
    print(resultado_funcion)