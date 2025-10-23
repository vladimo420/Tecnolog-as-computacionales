# Control y registro de calificaciones


### Contexto
-------------------
Tener un control a la hora de registrar las calificaciones tieje la funcion de realizar una evaluación de la calidad educativa: Permite a los educadores y a los padres de familia evaluar la efectividad de la enseñanza y la preparación de los estudiantes. Además de que tambíen ayuda a dectectar áreas donde existe deficiencia educativa en los estudiantes o donde los maestros necesitan una mayor capacticación .
Al igual es necesario a la hora de una distribucipon de los recursos con los datos de reprobación, pueden guíar la asignación de recursos educativos como personnal docente,  materiales e infraestructuras.

Los datos que rrgresara el problema para resolver el problema son:
-  Promedio de la clase total
- Almunos reprobados
- Alumnos acreditados

#####Referencias:
- https://www.superprof.mx/blog/la-educacion-en-mexico-y-la-cuestion-de-reprobar-ano/


###Algoritmo
    Eo _ Ingresar datos(cantidad_estudiantes, nombres, calificaciones, califi_aprobatoria)
            ingresa cantidad_estudiantes
            pide la cantidad de nombres en base a cantidad_estudiantes
            pide calificaciones en base a cantidad_estudiantes
    ​
           prom = calificaciones / cantidad_estudiantes
            
          
               mientras calificacionnes > califi_aprobatoria:
                       i  = 0
                       estudiantes_aprob=0
                                estudiantes_aprob = estudiantes_aprob+1
                                i = i + 1
                                     muestra (estudiantes_apro)
               
                mientras calificaciones < califi_aprobatoria:
                            i  = 0
                       estudiantes_repro=0
                                estudiantes_aprob = estudiantes_aprob+1
                                i = i +1
                                     muestra (estudiantes_repro)
                                                            
                                                            
    Ef_(prom, estudiantes_aprob, estudiantes_repro)
                       
 -------------------   
#### Módulos

######  -Modulo(Statistics)
En este proyecto el módulo statistics es utilizado que se uso con la funcion mean (statistics.mean), esto agiliza la operación que en este caso fue el promedio de las califaciones utilizadas solamente con una simple API haciendo más sencilla la forma de controlar los datos.
Esta API es utlizada dentro de la funcion calcular_promedio() dando así el proceso automatico para obtener el promedio del conjunto decalificaciones .

-Referencias: 
Python Software Foundation. (2024). statistics — Mathematical statistics functions.
In Python 3 Standard Library Documentation. Retrieved from
https://docs.python.org/3/library/statistics.html

-------------------

##### Instrucciones

1-Ejecuta en terminal
2-Ingresa todos los valores númericos


-------------------
