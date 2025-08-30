"""
código sencillo para algoritmo de operaciones con operadores
"""
print("información sobre concepto de suma")

#ejercicio

a=8
b=5
print("realiza el ejercicio con la suma de los siguientes valores")
print(a ,"y", b)

print("escribe el resultado de tu suma")
resultado_usuario=int(input())

suma=a+b

if resultado_usuario==suma:
 print("tu resultado es correcto")
elif resultado_usuario!=suma:
  print("tu resultado es incorrecto repite el proceso")
