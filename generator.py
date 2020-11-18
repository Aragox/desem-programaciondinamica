#!/usr/bin/python3

import sys
import copy
import random

id_problema = 1 # Datos generales del generador
nom_archivo = ""

letras = ['A','T','C','G'] # Datos para archivo de salida para secuencias
secuencia1 = ""
secuencia2 = ""

W = 0 # Datos para archivo de salida para mochila
N = 0
minPeso = 0
maxPeso = 0
minBeneficio = 0
maxBeneficio = 0
minCantidad = 0
maxCantidad = 0

############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
#Funciones para el problema de la mochila
#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################
def num_aleatorio(minimo, maximo):
    # Función que retorna un entero aleatorio dentro de un rango a partir de un máximo y mínimo
    # Entradas: mínimo (entero), máximo (entero)
    # Salida: entero
    if (minimo > maximo):
       return random.randint(maximo, minimo)
    return random.randint(minimo, maximo) 
    
def imprimir_salida1():
    # Función que imprime/crea un test del algoritmo mochila en un archivo de salida 
    try: #Abrir archivo de salida
        salida = open(str(nom_archivo), 'w')               
    except IOError:
        print ("\nError: No se logró crear o sobrescribir el archivo\n")
    else:
        print ("\nArchivo creado o modificado exitosamente\n")
        salida.write(str(W) + "\n") 
        for i in range(N):
            salida.write(str(num_aleatorio(minPeso, maxPeso)) + "," + str(num_aleatorio(minBeneficio, maxBeneficio)) + "," + str(num_aleatorio(minCantidad, maxCantidad)) + "\n")
        salida.close()
############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
#Funciones para el problema de alineamiento de secuencias
#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################    
def imprimir_salida2():
    # Función que imprime la salida 
    try: #Abrir archivo de salida
        salida = open(str(nom_archivo), 'w')               
    except IOError:
        print ("\nError: No se logró crear o sobrescribir el archivo\n")
    else:
        print ("\nArchivo creado o modificado exitosamente\n")
        salida.write(str(secuencia1) + "\n")
        salida.write(str(secuencia2) + "\n") 
        salida.close()

def crear_secuencia(largo):
    # Función que retorna una secuencia de letras aleatoria del largo solicitado
    #Entradas: largo (número entero)
    #Salidas: secuencia (string)
    secuencia = ""
    letra = ""
    for i in range(largo):
        letra = random.choice(letras)
        secuencia = secuencia + letra

    return secuencia

############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
#MAIN
#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################     
def main():
    global nom_archivo    
    global id_problema
    
    global secuencia1
    global secuencia2

    global W 
    global N 
    global minPeso 
    global maxPeso 
    global minBeneficio 
    global maxBeneficio 
    global minCantidad 
    global maxCantidad
    
    arg_valido = True 

    if (len(sys.argv) < 3):
        print("\nNúmero equivocado de argumentos\n")
        arg_valido = False # Número equivocado de argumentos
    
        if (len(sys.argv) == 1): # Si no se agregaron argumentos además del nombre del programa
            print("Sólo se recibió el nombre del programa\n")
        sys.exit() # Terminar programa

    if (not(sys.argv[1].isnumeric() and isinstance(sys.argv[2], str))): #Chequear tipos de argumento de línea de comandos
        print("\nTipo equivocado de argumentos (Primeros 3 argumentos deben ser: string int string)\n")
        arg_valido = False # Tipos equivocados
        
    else: # Tipos válidos (para los 3 primeros argumentos)
        id_problema = int(sys.argv[1])
        nom_archivo = sys.argv[2]

        if (id_problema not in [1,2]):
            print("\nEl valor del segundo argumento debe ser 1 ó 2\n")
            arg_valido = False # Tipos equivocados

        if (id_problema == 1): # Caso de mochila
            
            if (len(sys.argv) == 11): #Si el número de argumentos es igual a 11

                if (not(sys.argv[3].isnumeric()) and sys.argv[4].isnumeric() and sys.argv[5].isnumeric() and sys.argv[6].isnumeric() and sys.argv[7].isnumeric() and sys.argv[8].isnumeric() and sys.argv[9].isnumeric() and sys.argv[10].isnumeric()): #Chequear tipos de argumento de línea de comandos
                    print("\nTipo equivocado de argumentos (Se requiere: string int string int int int int int int int int)\n")
                    arg_valido = False # Tipos equivocados
                    
            else:
                print("\nNúmero equivocado de argumentos (Para mochila se requieren 11)\n")
                arg_valido = False # Número equivocado de argumentos

        if (id_problema == 2): # Caso de alineamiento de secuencias
            
            if (len(sys.argv) == 5): #Si el número de argumentos es igual a 5
                
                if (not(sys.argv[3].isnumeric() and sys.argv[4].isnumeric())): #Chequear tipos de argumento de línea de comandos
                    print("\nTipo equivocado de argumentos (Se requiere: string int string int int)\n")
                    arg_valido = False # Tipos equivocados
            else:
                print("\nNúmero equivocado de argumentos (Para alineamiento de secuencias se requieren 5)\n")
                arg_valido = False # Número equivocado de argumentos
                
    
    if (arg_valido): #El número y tipo de los argumentos es válido

        if (id_problema == 1): # Caso de mochila
            W = int(sys.argv[3])
            N = int(sys.argv[4])
            minPeso = int(sys.argv[5])
            maxPeso = int(sys.argv[6])
            minBeneficio =int(sys.argv[7])
            maxBeneficio = int(sys.argv[8])
            minCantidad = int(sys.argv[9])
            maxCantidad = int(sys.argv[10])

            imprimir_salida1()
            
        if (id_problema == 2): # Caso de alineamiento de secuencias

            secuencia1 = crear_secuencia(int(sys.argv[3])) #Crear secuencias
            secuencia2 = crear_secuencia(int(sys.argv[4]))

            imprimir_salida2() # Imprimir/generar archivo de salida

    #Imprimir datos de línea de comandos
    n = len(sys.argv) 
    print("Total de argumentos pasados:", n) 
  
    print("\nArgumentos pasados:", end = " ") 
    for i in range(0, n): 
        print(sys.argv[i], end = " ")
    print("\n")


if __name__ == "__main__":
    main()
