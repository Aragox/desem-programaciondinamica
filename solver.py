#!/usr/bin/python3

import sys
from fractions import Fraction
from decimal import Decimal
import copy
from itertools import combinations
from itertools import permutations
import csv

# Datos generales del solver
salida = None # Archivo de salida 
matriz = [] # Guarda los números
vector1 = [] #Vector de filas
vector2 = [] #Vector de columnas
id_problema = 1 # Determina el tipo de problema (mochila o alineamiento de secuencias)
algoritmo = 1 # Determinar si se resuelve por algoritmo de fuerza bruta o programación dinámica
nom_archivo = "" # Nombre de archivo de salida

# Variables para el problema de mochila
lista_objetos = []
peso_max = -1
beneficio_max = -1

# Variables para el problema de secuencias
secuencia1 = ""
secuencia2 = ""
scorefinal = 0

resultados = []
        
###########################################################################################################
#----------------------------------------------------------------------------------------------------------
#   Clase Ítem
#----------------------------------------------------------------------------------------------------------
##########################################################################################################        
class Articulo:
#Clase Fracción
    def __init__(self, tipo, peso, beneficio):
        # Constructor, asigna el tipo de articulo como entero, el peso como entero y el beneficio como entero
        self.tipo = tipo
        self.peso = peso
        self.beneficio = beneficio
            
    def get_tipo(self):
        #Función que retorna el tipo del artículo
        return self.tipo

    def get_peso(self):
        #Función que retorna el peso del artículo
        return self.peso

    def get_beneficio(self):
        #Función que retorna el beneficio del artículo
        return self.beneficio

    def __str__(self):
        # Función que retorna el artículo como un string
        return '[%s, %s, %s]' %(self.tipo, self.peso, self.beneficio)
    
###########################################################################################################
#----------------------------------------------------------------------------------------------------------
#   Clase Nodo
#----------------------------------------------------------------------------------------------------------
##########################################################################################################        
class Nodo:
#Clase Fracción
    def __init__(self, valor, diag, izq, arriba):
        # Constructor, asigna el valor al nodo y las direcciones
        self.valor = valor
        self.dir = [diag,izq,arriba]
            
    def get_valor(self):
        #Función que retorna el valor del nodo
        return self.valor

    def get_dir(self):
        #Función que retorna el vector de direcciones del nodo
        return self.dir

    def get_diagonal(self):
        #Función que retorna la dirección diagonal
        return self.dir[0]
        
    def get_izquierda(self):
        #Función que retorna la dirección izquierda
        return self.dir[1]

    def get_arriba(self):
        #Función que retorna la dirección arriba
        return self.dir[2]

    def set_valor(self, valor):
        #Función que setea el valor del nodo
        self.valor = valor     
###########################################################################################################
#----------------------------------------------------------------------------------------------------------
#   Manual del programa (-h)
#----------------------------------------------------------------------------------------------------------
###########################################################################################################

def manual():
    print("\n")    
    print("##########################################################################################################")
    print("----------------------------------------------------------------------------------------------------------")
    print("Inicio Sección Ayuda")
    print("----------------------------------------------------------------------------------------------------------")
    print("##########################################################################################################")
    print("\nEstudiante-> Ricardo Víquez Mora\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("\nDESCRIPCIÓN DEL PROGRAMA:")
    print("Este programa consiste en una serie de implementaciones de algoritmos tanto de fuerza bruta como de programación")
    print("dinámica, con el objetivo de medir su desempeño. Se soluciona el problema de la mochila y el problema de ordenamiento")
    print("de secuencias.\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("\nCÓMO USAR EL PROGRAMA:")
    print("- Si no se ha hecho, colocar los archivos 'solver.py' y 'generator.py' en el mismo directorio que los archivos de los problemas a")
    print("resolver en formato (.txt)")
    print("- Ejecutar terminal dentro del mismo directorio")
    print("- En la terminal, escribir los parámetros correspondientes de línea de comandos (ver sección 'PARÁMETROS DE LÍNEA DE COMANDOS')")
    print("- Presionar la tecla ENTER para ejecutar el programa")
    print("- Para el módulo 'solver', tanto los algoritmos de la mochila, como los de ordenamiento de secuencias, imprimen")
    print("la respuesta en la terminal y guardan parte de la respuesta en un archivo de salida")
    print("- Para el módulo 'generator', tanto el problema de la mochila, como el de ordenamiento de secuencias, generan")
    print("un experimento en un archivo de entrada para el 'solver'")
    print("\nNota 1:")
    print("Para el problema de la mochila, la solución se guarda automáticamente en un archivo siguiendo el siguiente formato:")
    print("\n    nombre_archivo_entrada + '_M_resp' + ('FB' o 'PD').txt\n")
    print("Donde:")
    print("- 'nombre_archivo_entrada' es el nombre del archivo de entrada.")
    print("- '_M_resp' es parte del sufijo agregado al archivo de salida\n")
    print("- 'FB' sufijo es agregado si se resolvió el problema usando el algoritmo de Fuerza Bruta\n")
    print("- 'PD' sufijo es agregado si se resolvió el problema usando el algoritmo de Programación Dinámica\n")
    print("\nNota 2:")
    print("Para el problema de ordenamiento de secuencias, la solución se guarda automáticamente en un archivo siguiendo el siguiente formato:")
    print("\n    nombre_archivo_entrada + '_AS_resp' + ('FB' o 'PD').txt\n")
    print("Donde:")
    print("- 'nombre_archivo_entrada' es el nombre del archivo de entrada.")
    print("- '_AS_resp' es parte del sufijo agregado al archivo de salida\n")
    print("- 'FB' es agregado si se resolvió el problema usando el algoritmo de Fuerza Bruta\n")
    print("- 'PD' es agregado si se resolvió el problema usando el algoritmo de Programación Dinámica\n")
    print("\nNota 3:")
    print("Además, para el problema de ordenamiento de secuencias:")
    print("- En el caso de FB, en la teminal se imprimen también las soluciones que empataron con la mejor solución")
    print("- En el caso de PD, el archivo de salida es un .csv y contiene sólamente una tabla, y la solución se imprime en la terminal")
    print("----------------------------------------------------------------------------------------------------------")
    print("\nPARÁMETROS DE LÍNEA DE COMANDOS:")
    print("Los parámetros del módulo 'solver' son los siguientes:")
    print("\n    python3 solver.py [-h] PROBLEMA ALGORITMO ARCHIVO\n")     
    print("Donde:")
    print("- El parámetro 'solver.py' es el nombre del archivo ejecutable.")
    print("- El parámetro '-h' es opcional, y muestra una descripción de como usar el programa, parámetros y formato de")
    print("archivo de entrada.")
    print("- El parámetro 'PROBLEMA' es valor de 1 o 2, indicando el problema a resolver, 1 mochila, 2 alineamiento.")
    print("- El parámetro 'ALGORITMO' es valor de 1 o 2, indicando el algoritmo a usar, 1 fuerza bruta, 2 programación dinámica.")
    print("- El parámetro 'ARCHIVO' es el nombre del archivo de entrada")
    print("\nLos parámetros del módulo 'generator' son los siguientes:")
    print("\n    python3 generator.py PROBLEMA ARCHIVO PARÁMETROS\n")     
    print("Donde:")
    print("- El parámetro 'generator.py' es el nombre del archivo ejecutable.")
    print("- El parámetro 'PROBLEMA' es valor de 1 o 2, indica el problema de cual generar datos, 1 mochila, 2 alineamiento.")
    print("- El parámetro 'ARCHIVO' es el nombre del archivo de entrada")
    print("- El parámetro 'PARÁMETROS' se detallan en cada problema más adelante. Estos varían con respecto a cada problema.")
    print("\n'PARÁMETROS' del módulo 'generator' para el problema de la mochila:")
    print("\n    W N minPeso maxPeso minBeneficio maxBeneficio minCantidad maxCantidad\n")     
    print("Donde:")
    print("- El parámetro 'W' es el peso soportado por la mochila.")
    print("- El parámetro 'N' es la cantidad de elementos.")
    print("- minPeso,maxPeso indica el valor mínimo y máximo para asignar el peso aleatorio a un elemento.")
    print("- minBeneficio,maxBeneficio indica el valor mínimo y máximo para asignar el beneficio aleatorio a un elemento.")
    print("- minCantidad,maxCantidad indica el valor mínimo y máximo para asignar la cantidad disponible de un elemento.")
    print("\n'PARÁMETROS' del módulo 'generator' para el problema del alineamiento de secuencias:")
    print("\n    largoH1 largoH2\n")     
    print("Donde:")
    print("- El parámetro 'largoH1' es el largo de la hilera 1")
    print("- El parámetro 'largoH2' es el largo de la hilera 2")
    print("\n")
    print("##########################################################################################################")
    print("----------------------------------------------------------------------------------------------------------")
    print("Final Sección Ayuda")
    print("----------------------------------------------------------------------------------------------------------")
    print("##########################################################################################################")
    print("\n")
    
def inicializar_matriz():
    #Función que inicializa la matriz con enteros
    global matriz
    matriz=[] #Vaciar matriz
    
    for i in range(len(vector1)): #Total de filas
        row=[] #Fila
        for j in range(len(vector2)): #Total de columnas
            row.append(0) #Añadir 0 para cada columna de esta fila
        matriz.append(row) #Añadir fila definida a la matriz

def inicializar_matriz_nodos():
    #Función que inicializa la matriz con nodos de valor cero y vector de direcciones [0,0,0]
    global matriz
    matriz=[] #Vaciar matriz
    
    for i in range(len(vector1)): #Total de filas
        row=[] #Fila
        for j in range(len(vector2)): #Total de columnas
            row.append(Nodo(0,0,0,0)) #Añadir valores para cada columna de esta fila
        matriz.append(row) #Añadir fila definida a la matriz

def imprimir_matriz():
    # Función que imprime en terminal la variable global matriz, en un formato más agradable
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (isinstance(matriz[i][j], int)): # Si el objeto es un entero
                print(str(matriz[i][j]) + " ", end = '')            
            elif (isinstance(matriz[i][j], Nodo)):  # Si el objeto es un nodo
                print(str(matriz[i][j].get_valor())+ " ", end = '')
        print("")
        
def imprimir_salida_mochila(resultado):
    # Función que imprime la salida del problema de mochila para fuerza bruta
    global beneficio_max

    if resultado:
        beneficio_max = resultado[0]
        articulos = [] # Lista de pares ordenados de valores con la forma: [tipo artículo, cantidad del artículo]
        resultado = resultado[1:]
        cont_id = resultado[0]
        cont_articulos = 0
        
        i = 0
        while (i < len(resultado)): # Obtener pares ordenados
            if (resultado[i] == cont_id):
                cont_articulos = cont_articulos + 1
                i = i + 1
            else:
                if (cont_articulos >= 1):
                    articulos.append([cont_id, cont_articulos]) # Agregar par ordenado
                cont_id = resultado[i] # Cambiar al siguiente artículo
                cont_articulos = 0

        if (cont_articulos >= 1):
            articulos.append([cont_id, cont_articulos]) # Agregar el par ordenado faltante
        
        try: #Abrir archivo de salida
            
           if (algoritmo == 1): # Selecciona el formato del archivo según el algoritmo
               terminacion = '_M_respFB'
           elif (algoritmo == 2):
               terminacion = '_M_respPD'
               imprimir_matriz() #Imprime tabla final
               print("")
               
           salida = open(str(nom_archivo) + terminacion, 'w')               
        except IOError:
            print ("Error: No se logró crear o sobrescribir el archivo\n")
        else:
            print ("Archivo creado o modificado exitosamente\n")
             
            print(beneficio_max) # Imprimir solución en terminal y en archivo de salida
            salida.write(str(beneficio_max) + "\n")
            for i in range(len(articulos)):
                print(str(articulos[i][0]) + "," + str(articulos[i][1]) + " #articulo " + str(articulos[i][0]) + " " + str(articulos[i][1]) + " unidades")
                salida.write(str(articulos[i][0]) + "," + str(articulos[i][1]) + " #articulo " + str(articulos[i][0]) + " " + str(articulos[i][1]) + " unidades" + "\n")
            
    else:
        print("No hay artículos definidos correctamente en el archivo de entrada")

def imprimir_salida_alineamiento():
    # Función que imprime la salida del problema de alineamiento de secuencias para fuerza bruta
    try: #Abrir archivo de salida
        salida = open(str(nom_archivo) + '_AS_respFB', 'w')               
    except IOError:
        print ("Error: No se logró crear o sobrescribir el archivo\n")
    else:
        print ("Archivo creado o modificado exitosamente\n")
            
        for elem in resultados: # Imprime los empates
            if (elem[2] == scorefinal): # Imprimir sólo las comparaciones que empataron con el mejor puntaje
                print("".join(elem[0]) + ", " + "".join(elem[1]) + ", " + str(elem[2])) # Imprimir en terminal
                salida.write("".join(elem[0]) + ", " + "".join(elem[1]) + ", " + str(elem[2]) + "\n") # Guardar en archivo
                    
        print("") # Imprimir en terminal                
        print("Score Final: "+ str(scorefinal))
        print("Hilera1: "+ secuencia1)
        print("Hilera2: "+ secuencia2)                
        salida.write("\n") # Guardar en archivo 
        salida.write("Score Final: "+ str(scorefinal) + "\n")
        salida.write("Hilera1: "+ secuencia1 + "\n")
        salida.write("Hilera2: "+ secuencia2 + "\n")
            
        salida.close() # Cerrar archivo

def imprimir_salida_alineamiento2():
    # Función que imprime la salida del problema de alineamiento de secuencias para programación dinámica.
    # Imprime una parte de la salida en la terminal, y otra en una tabla .csv
    # (Se usó de referencia código de https://www.geeksforgeeks.org/writing-csv-files-in-python/)

    print("") # Imprimir en terminal                
    print("Score Final: "+ str(scorefinal))
    print("Hilera1: "+ secuencia1)
    print("Hilera2: "+ secuencia2) 
    
    # Nombres de campos
    campos = list(" ") + vector2  
    
    # Filas del archivo csv 
    filas = []
    for i in range(len(matriz)):
        contenido = []
        for j in range(len(matriz[0])):
            contenido.append(str(matriz[i][j].get_valor()))
        filas.append(list(vector1[i]) + contenido)
    
    # Nombre del archivo csv   
    filename = str(nom_archivo) + '_AS_respPD.csv'
    
    # Escribir en archivo csv  
    with open(filename, 'w') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(campos)   
        csvwriter.writerows(filas)

def comparacion(indice1,indice2):
    #Función que compara 2 caracteres obtenidos de 2 vectores, y retorna una puntuación (Para el algoritmo de programación dinámica)
    if (vector1[indice1] == vector2[indice2]):
        return 1
    return -1

def string_reverso(s):
    # Función que retorna un string en orden al revés.
    s1 = ""
    for i in s:
        s1 = i + s1
    return s1
    
def puntajetotal(elem1, elem2):
    # Función que retorna el puntaje correspondiente a comparar 2 secuencias (Para el algoritmo de fuerza bruta)
    score = 0
    for i in range(len(elem1)):
        if (elem1[i] == elem2[i] and elem1[i] != '_'):
            score = score + 1
        elif (elem1[i] != elem2[i] and elem1[i] != '_' and elem2[i] != '_'):
            score = score - 1
        elif (elem1[i] == '_' and elem2[i] != '_'):
            score = score - 2
        elif (elem1[i] != '_' and elem2[i] == '_'):
            score = score - 2
        elif (elem1[i] == elem2[i] and elem1[i] == '_'):
            score = score - 4
    return score

def mejor_resultado():
    # Función que retorna una lista con la secuencia1 y la secuencia2 y la mayor puntuación
    resultado = copy.deepcopy(resultados[0])
    for i in range(len(resultados)):
        if (resultados[i][2] > resultado[2]):
            resultado = copy.deepcopy(resultados[i])
            
    return resultado           
    
############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
#   MAIN
#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################     
def main():
    
    global matriz # Para trabajar con variables globales
    global vector1
    global vector2
    global salida
    global id_problema 
    global algoritmo
    global nom_archivo

    global lista_objetos
    global peso_max
    global beneficio_max
    
    global secuencia1
    global secuencia2
    global scorefinal
    global resultados
    
    arg_valido = True

    if (len(sys.argv) == 2 and sys.argv[1] == "-h"): #Si hay opción -h
        arg_valido = False
        manual()

    elif (len(sys.argv) == 2 and sys.argv[1] != "-h"): #Si largo 2 pero no hay opción -h
        arg_valido = False
        print("\nPara ver 'ayuda' el argumento #2 debe ser '-h'\n")

    if (len(sys.argv) == 4): #Si el número de argumentos es igual a 4
        
        if (not(sys.argv[1].isnumeric() and sys.argv[2].isnumeric() and isinstance(sys.argv[3], str))): #Chequear tipos de argumento de línea de comandos
            print("\nTipo equivocado de argumentos (Para la 'resolución' se requiere: string int int string)\n")
            arg_valido = False # Tipos equivocados

    if (len(sys.argv) != 2 and len(sys.argv) != 4):
        arg_valido = False # Número equivocado de argumentos
        print("\nNúmero equivocado de argumentos (Para 'ayuda' se requieren 2, para la 'resolución' se requieren 4)\n")
        
        if (len(sys.argv) == 1): # Si no se agregaron argumentos además del nombre del programa
            print("Sólo se recibió el nombre del programa\n")

    if (arg_valido): #El número y tipo de los argumentos es válido
       id_problema = int(sys.argv[1]) # Obtener datos de línea de comandos
       algoritmo = int(sys.argv[2])
       nom_archivo = sys.argv[3]
        
       lineas = []
       try:
           entrada = open(sys.argv[3],"r")        
           lineas = entrada.readlines() # Obtiene todas las líneas del archivo de entrada        
       except IOError:
          print ("\nError: No se logró encontrar/abrir el archivo\n")
          sys.exit() # No se logró abrir el archivo del parámetro nom_archivo
       else:
          print ("\nDatos extraídos exitosamente del archivo\n")
          entrada.close()
        
       for i in range(len(lineas)): # Quitar comillas de las lineas
           lineas[i] = lineas[i].split(',')
           
############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
#   Ejecución Mochila
#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################
       if (id_problema == 1): # Mochila
           peso_max = int(lineas[0][0])
           cont = 1
           while (cont < len(lineas)):
               peso = int(lineas[cont][0])
               beneficio = int(lineas[cont][1])
               cantidad = int(lineas[cont][2])
               for i in range(cantidad):
                   lista_objetos.append(Articulo(cont,peso,beneficio))
               cont = cont + 1

#---------------------------------------------------------------------------------------------------------------------------
#   Mochila (F.Bruta)
#---------------------------------------------------------------------------------------------------------------------------
           if (algoritmo == 1): # (F.Bruta)
               combinaciones = [] # Guarda las combinaciones de los artículos
               for i in list(range(len(lista_objetos))): # Guardar todas las combinaciones de distinto largo
                   combinaciones.append(combinations(lista_objetos, i+1))
               combinaciones = [i for fila in combinaciones for i in fila] # Aplanar la lista de combinaciones

               resultados = []
               for i in range(len(combinaciones)): # Obtener el mejor resultado
                   sumapeso = 0
                   sumabeneficio = 0
                   tipos = []
                   combinaciones[i] = list(combinaciones[i]) # Convertir de tupla a lista
                   for j in range(len(combinaciones[i])):
                       tipos.append(combinaciones[i][j].get_tipo()) # Guardar el tipo del artículo
                       sumapeso = sumapeso + combinaciones[i][j].get_peso() # Acumula peso
                       sumabeneficio = sumabeneficio + combinaciones[i][j].get_beneficio() # Acumula beneficio
                       
                   if (sumapeso <= peso_max): # Si el peso acumulado es menor o igual al peso máximo soportado
                       tipos.sort() # Ordenar ascendentemente los tipos de artículos
                       resultados.append([sumabeneficio] + tipos) # Guardar el beneficio acumulado y los artículos utilizados
                       
               mejorcombinacion = [] # Guarda el mejor resultado para el problema de la mochila       
               if resultados: # Si resultados no está vacío
                   mejorcombinacion = copy.deepcopy(resultados[0])
                   
               for i in range(len(resultados)): # Obtener el mejor resultado para el problema de la mochila
                   if (resultados[i][0] > mejorcombinacion[0]): # Si hay una mejor solución
                       mejorcombinacion = copy.deepcopy(resultados[i])

               imprimir_salida_mochila(mejorcombinacion) # Guardar en archivo de salida
                       
#---------------------------------------------------------------------------------------------------------------------------
#   Mochila (P.Dinámica)
#---------------------------------------------------------------------------------------------------------------------------                  
           if (algoritmo == 2): # (P.Dinámica)
               for i in range(len(lista_objetos)+1): # Construir el vector de los artículos (filas)
                   vector1.append(i) 
               for i in range(peso_max+1): # Construir el vector de los pesos (columnas)
                   vector2.append(i)
               
               inicializar_matriz()

               for k in range(1, len(lista_objetos)+1): # Algoritmo visto en clase
                   for w in vector2:                      
                       if (lista_objetos[k-1].get_peso() > w): # Si el peso del artículo es mayor que el peso en la tabla
                           matriz[k][w] = matriz[k-1][w]
                       else:
                           if (lista_objetos[k-1].get_beneficio() + matriz[k-1][w-lista_objetos[k-1].get_peso()] > matriz[k-1][w]):
                               matriz[k][w] = lista_objetos[k-1].get_beneficio() + matriz[k-1][w-lista_objetos[k-1].get_peso()]
                           else:
                               matriz[k][w] = matriz[k-1][w]

               beneficio_max = matriz[len(matriz)-1][len(matriz[0])-1] # Obtener el beneficio máximo           

               tipos = [] # Lista de tipos de artículos a guardar
               i = len(matriz)-1
               k = len(matriz[0])-1

               cont = i
               while (i > 0 and k >= 0): # Mientras no se hayan abarcado todas las filas, anotar cuáles artículos se añadieron a la mochila
                   if (matriz[i][k] != matriz[i-1][k]): # Artículo añadido
                       tipos.append(lista_objetos[cont-1].get_tipo()) # Guardar el tipo del artículo
                       i = i - 1
                       k = k - lista_objetos[cont-1].get_peso()
                   else: # No se incluyó el artículo
                       i = i - 1
                   cont = cont - 1
                       
               tipos.sort() # Ordenar ascendentemente los tipos de artículos
               mejor_resultado = [beneficio_max] + tipos
               imprimir_salida_mochila(mejor_resultado) # Guardar en archivo de salida
               
############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
#   Ejecución alineamiento de secuencias
#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################
       if (id_problema == 2): # Alineamiento de Secuencias
           
           secuencias = []
           
           for line in lineas: # Obtener secuencias en forma de string
               str1 = " "
               elem = str1.join(line)
               secuencias.append(elem.rstrip())
               
           secuencia1 = secuencias[0]
           secuencia2 = secuencias[1]
#---------------------------------------------------------------------------------------------------------------------------
#   Alineamiento de secuencias (F.Bruta)
#---------------------------------------------------------------------------------------------------------------------------           
           if (algoritmo == 1): #(F.Bruta)
               
               mayor = len(secuencia2) # Guarda el largo de la secuencia de entrada más corta
               
               if (len(secuencia1) > len(secuencia2)):
                   mayor = len(secuencia1)
                   
               k = len(secuencia1) + len(secuencia2) # Obtener el número máximo de gaps
               
               resultados = [] # Contiene todas las comparaciones entre permutaciones y sus puntajes respectivos
               while (k >= mayor): # Probar con diferente número de gaps
                   gaps1 = k - len(secuencia1) # Obtener número de gaps a permutar
                   gaps2 = k - len(secuencia2)
                   perm1 = list(set(permutations(('A'*len(secuencia1)) + ('_'*gaps1)))) # Permutar largo de la secuencia (un mismo símbolo) + gaps, y remover permutaciones repetidas
                   cont = 0
                   for i in range(len(perm1)): # Sustituir símbolos repetidos por bases nitrogenadas de la secuencia1
                       perm1[i] = list(perm1[i]) # Convertir tupla a lista
                       for j in range(len(perm1[0])):
                           if (perm1[i][j] == 'A'):
                               perm1[i][j] = secuencia1[cont]
                               cont = cont + 1
                       cont = 0
                   perm2 = list(set(permutations(('A'*len(secuencia2)) + ('_'*gaps2)))) # Permutar largo de la secuencia (un mismo símbolo) + gaps, y remover permutaciones repetidas
                   cont = 0
                   for i in range(len(perm2)): # Sustituir símbolos repetidos por bases nitrogenadas de la secuencia2
                       perm2[i] = list(perm2[i]) # Convertir tupla a lista
                       for j in range(len(perm2[0])):
                           if (perm2[i][j] == 'A'):
                               perm2[i][j] = secuencia2[cont]
                               cont = cont + 1
                       cont = 0
                   for elem1 in perm1: # Comparar las secuencias obtenidas de cada permutación
                       for elem2 in perm2:
                           puntaje = puntajetotal(elem1, elem2) # Obtener el puntaje de la comparación de 2 secuencias 
                           resultado = [elem1, elem2, puntaje]
                           resultados.append(resultado) # Guardar las secuencias que se compararon y el puntaje respectivo
                           
                   k = k - 1 # Reducir K                     
                       
               resfinal = mejor_resultado() # Obtener el alineamiento con el mayor puntaje
               secuencia1 = "".join(resfinal[0])
               secuencia2 = "".join(resfinal[1])
               scorefinal = resfinal[2]
                   
               imprimir_salida_alineamiento() # Guardar en archivo de salida 
#---------------------------------------------------------------------------------------------------------------------------
#   Alineamiento de secuencias (P.Dinámica)
#---------------------------------------------------------------------------------------------------------------------------               
           if (algoritmo == 2): #(P.Dinámica)
               s1 = copy.deepcopy(secuencia1) # Hacer copia profunda
               s2 = copy.deepcopy(secuencia2)
               
               vector1 = list(' '+s2) # Agregar el caracter vacío al inicio de los vectores
               vector2 = list(' '+s1)
               
               inicializar_matriz_nodos() #inicializar matriz con nodos

               cont = 0
               for i in range(len(vector2)): # Asignar los nodos que resultan de incluir vacío en una comparación
                   matriz[0][i] = Nodo(-1*cont,0,1,0)
                   cont = cont + 2
                   
               cont = 0
               for i in range(len(vector1)): # Asignar los nodos que resultan de incluir vacío en una comparación
                   matriz[i][0] = Nodo(-1*cont,0,0,1)
                   cont = cont + 2

               cont1 = 1
               while (cont1 < len(vector1)): # Asignar los nodos con el valor y direcciones respectivas con base en la fórmula
                   cont2 = 1
                   while (cont2 < len(vector2)):
                       res1 = matriz[cont1 - 1][cont2 - 1].get_valor() + comparacion(cont1,cont2) # Fórmula
                       res2 = matriz[cont1][cont2 - 1].get_valor() + -2
                       res3 = matriz[cont1 - 1][cont2].get_valor() + -2
                       vector = [res1, res2, res3]
                       
                       mayor = max(res1, res2, res3) # Guardar el resultado mayor
                       
                       matriz[cont1][cont2] = Nodo(mayor,0,0,0) # Inicializar Nodo
                       for i in range(3):
                           if (mayor == vector[i]): # Asignar las direcciones en el Nodo con base al resultado mayor
                               matriz[cont1][cont2].dir[i] = 1
                                                                   
                       cont2 = cont2 + 1
                       
                   cont1 = cont1 + 1
                   
               secuencia1 = ""
               secuencia2 = "" 
               cont1 = len(matriz) - 1
               cont2 = len(matriz[0]) - 1

               while (cont1 > 0 or cont2 > 0): # Recorrer la ruta de la matriz (del final al inicio)
                           
                   if (matriz[cont1][cont2].get_diagonal()==1): # Se escoge el camino de la diagonal
                       secuencia1 = secuencia1 + vector2[cont2]
                       secuencia2 = secuencia2 + vector1[cont1]
                       cont1 = cont1 - 1
                       cont2 = cont2 - 1
                   elif (matriz[cont1][cont2].get_izquierda()==1): # Se escoge el camino de la izquierda                     
                         secuencia1 = secuencia1 + vector2[cont2]
                         secuencia2 = secuencia2 + "_"                        
                         cont2 = cont2 - 1                       
                   elif (matriz[cont1][cont2].get_arriba()==1): # Se escoge el camino de arriba                     
                         secuencia1 = secuencia1 + "_"
                         secuencia2 = secuencia2 + vector1[cont1]                        
                         cont1 = cont1 - 1


               secuencia1 = string_reverso(secuencia1) # Obtener el reverso de las secuencias
               secuencia2 = string_reverso(secuencia2)

               scorefinal = matriz[len(matriz)-1][len(matriz[0])-1].get_valor() # Obtener score final del alineamiento

               imprimir_salida_alineamiento2() # Guardar en archivo de salida 

    #Imprimir datos de línea de comandos
    n = len(sys.argv) 
    print("\nTotal de argumentos pasados:", n) 
  
    print("\nArgumentos pasados:", end = " ") 
    for i in range(0, n): 
        print(sys.argv[i], end = " ")
    print("\n")


if __name__ == "__main__":
    main()
