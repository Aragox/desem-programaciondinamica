#!/usr/bin/python3

import sys
from fractions import Fraction
from decimal import Decimal
import copy 

salida = None # Archivo de salida

 # Datos para archivo de salida

matriz = [] # Guarda los números de la tabla actual

###########################################################################################################
#----------------------------------------------------------------------------------------------------------
#   Clase Fracción y métodos
#   Se usó de referencia la clase "Fraction" implementada por msarialp en https://gist.github.com/mustaa/2350807
#----------------------------------------------------------------------------------------------------------
##########################################################################################################
def gcd(num, denom):
#Función que retorna el máximo común divisor
    if (num == 0 or denom == 0):
        return 1
    
    while num != denom:
        if num > denom:
            num = num - denom
        else:
            denom = denom - num
    return num

class Fraccion:
#Clase Fracción
    def __init__(self, num, denom):
        # Constructor, recibe el numerador y denominador, para luego simplificar la fracción
        self.simplificar(num, denom)
        
    def simplificar(self, num, denom):
        # Función que simplifica la fracción usando el máximo común divisor. Asigna los nuevos valores al numerador y denominador
        self.num = int(num / gcd(abs(num), abs(denom)))
        self.denom = int(denom / gcd(abs(num), abs(denom)))
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1*self.num
        elif self.denom == 0:
            raise ZeroDivisionError
        elif self.num == 0:
            self.denom = 1
            
    def simplificar_nomod(self, num, denom):
        # Función que simplifica la fracción (sin modificar al asignar) usando el máximo común divisor.
        #Retorna los nuevos valores al numerador y denominador en una tupla
        num1 = int(num / gcd(abs(num), abs(denom))) # Simplificar numerador y denominador
        denom1 = int(denom / gcd(abs(num), abs(denom)))
        if denom1 < 0: # Posibles cambios de signo de numerador y denominador
            denom1 = abs(denom1)
            num1 = -1*num1
        elif denom1 == 0: # Se indefine la fracción
            raise ZeroDivisionError
        elif num1 == 0:
            denom1 = 1
        return num1, denom1 # Retornar tupla
        
    def sum(self, other):
        # Función que suma 2 fracciones. Actualiza el resultado en la fracción izquierda 
        num = self.num*other.denom + self.denom*other.num
        denom = self.denom*other.denom
        self.simplificar(num, denom)
    
    def sub(self, other):
        # Función que resta 2 fracciones. Actualiza el resultado en la fracción izquierda
        num = self.num*other.denom - self.denom*other.num
        denom = self.denom*other.denom
        self.simplificar(num, denom)

    def sub_nomod(self, other):
        # Función que resta 2 fracciones. No realiza modificaciones a la fracción izquierda. Retorna una tupla [numerador,denominador] simplificados
        num = self.num*other.denom - self.denom*other.num # Guardar resultado de la resta
        denom = self.denom*other.denom
        return self.simplificar_nomod(num, denom) # Retornar tupla
    
    def mul(self, other):
        # Función que multiplica 2 fracciones. Actualiza el resultado en la fracción izquierda
        num = self.num*other.num
        denom = self.denom*other.denom
        self.simplificar(num, denom)
    
    def div(self, other):
        # Función que divide 2 fracciones. Actualiza el resultado en la fracción izquierda
        num = self.num*other.denom
        denom = self.denom*other.num
        self.simplificar(num, denom)

    def div_nomod(self, other):
        # Función que divide 2 fracciones. No realiza modificaciones a la fracción izquierda. Retorna una tupla [numerador,denominador] simplificados
        num = self.num*other.denom # Guardar resultado de la división
        denom = self.denom*other.num
        return self.simplificar_nomod(num, denom) # Retornar tupla

    def comparar(self, other):
        # Función que compara 2 fracciones para determinar cuál es mayor.
        #No realiza modificaciones. Retorna True si la fracción de la derecha es mayor, y False en caso contrario
        tupla = self.sub_nomod(other)
        numero = tupla[0]
        if (numero >= 0):
            return False
        return True

    def get_num(self):
        #Función que retorna el numerador de la fracción
        return self.num

    def get_denom(self):
        #Función que retorna el denominador de la fracción
        return self.denom    

    def __str__(self):
        # Función que retorna la fracción como un string 
        if self.denom == 1 or self.num == 0:
            return str(self.num)
        else:
            return '%s/%s' %(self.num, self.denom)

###########################################################################################################
#----------------------------------------------------------------------------------------------------------
#    Final de sección de código
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
    print("Este programa es una implementación del método simplex para resolver problemas de minimización y maximización")
    print("en programación lineal.\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("\nCÓMO USAR EL PROGRAMA:")
    print("- Si no se ha hecho, colocar este archivo en el mismo directorio que los archivos de los problemas a")
    print("resolver en formato (.txt)")
    print("- Ejecutar terminal dentro del mismo directorio")
    print("- En la terminal, escribir los parámetros correspondientes de línea de comandos (ver sección 'PARÁMETROS DE LÍNEA DE COMANDOS')")
    print("- Presionar la tecla ENTER para ejecutar el programa")
    print("\nNota: La solución, con los pasos intermedios se guarda automáticamente en un archivo .txt siguiendo el siguiente formato:")
    print("\n    nombre_archivo_entrada + _solution.txt\n")
    print("Donde:")
    print("- 'nombre_archivo_entrada' es el nombre del archivo de entrada.")
    print("- '_solution.txt' es el sufijo agregado al archivo de salida\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("\nPARÁMETROS DE LÍNEA DE COMANDOS:")   
    print("\n    python simplex.py [-h] archivo.txt\n")     
    print("Donde:")
    print("- El parámetro 'simplex.py' es el nombre del archivo ejecutable.")
    print("- El parámetro '-h' es opcional, y muestra una descripción de como usar el programa, parámetros y formato de")
    print("archivo de entrada.")
    print("- El parámetro 'archivo.txt' es el nombre del archivo de entrada (No se debe de incluir la extensión (.txt)")
    print("en este parámetro).")
    print("\n\nFORMATO DE ARCHIVO DE ENTRADA:")
    print("La estructura del archivo de entrada consiste en elementos separados por coma y en diferentes líneas/filas")
    print("de la siguiente forma:")
    print("\n    método, optimización, Número de variables de decisión, Número de restricciones\n")
    print("\n    coeficientes de la función objetivo\n")
    print("\n    coeficientes de la restricción, signo de restricción, número en la derecha de la restricción\n")
    print("Donde:")
    print("- 'método' es un entero [ 0=Simplex, 1=GranM, 2=DosFases], que es el método para resolver el problema")    
    print("- 'optimización' se indica con min o max, y es el tipo de optimización deseada en el problema")
    print("- 'Número de variables de decisión' es un entero, y es el número de variables del problema")
    print("- 'Número de restricciones' es un entero, y es el número de restricciones del problema")
    print("- 'coeficientes de la función objetivo' son valores numéricos separados por comas, y son los coeficientes")
    print("de la función objetivo")
    print("- 'coeficientes de la restricción' son valores numéricos separados por comas, y son los coeficientes")
    print("de la restricción")
    print("- 'signo de restricción' es un símbolo ['<=', '>=', '='], e indica el tipo de inecuación")
    print("- 'número en la derecha de la restricción' es un valor numérico, y es el número en la derecha de la restricción")
    print("\nNota: Se pueden añadir en distintas líneas tantas restricciones como las indicadas en 'Número de restricciones'")
    print("\n")
    print("##########################################################################################################")
    print("----------------------------------------------------------------------------------------------------------")
    print("Final Sección Ayuda")
    print("----------------------------------------------------------------------------------------------------------")
    print("##########################################################################################################")
    print("\n")
    
def inicializar_matriz():
    #Función que inicializa la matriz con ceros
    global matriz
    matriz=[] #Vaciar matriz
    
    for i in range(len(nombre_filas)): #Total de filas
        row=[] #Fila
        for j in range(len(nombre_columnas) - 1): #Total de columnas
            row.append(Fraccion(0,1)) #Añadir Fracción 0/1 para cada columna de esta fila
        matriz.append(row) #Añadir fila definida a la matriz

def menor_fraccion(lst):
    #Función que retorna el objeto fracción correspondiente al valor menor de una lista de fracciones
    menor = lst[0]
    for i in range(len(lst)):
        elem = lst[i]
        if (Fraccion.comparar(elem, menor)): # Si menor actual es mayor que el elem
            menor = elem

    return menor

def menor_coeficienteObjetivo():
    #Función que retorna la posición del coeficiente mínimo de la función objetivo,
    #lo que permite obtener la posición de la columna pivote
    res = copy.deepcopy(matriz[0])
    fila = res[:len(res)-1] # No se incluye la columna LD
    f = menor_fraccion(fila)
    return buscar_fraccion(fila, f) # Retorno la posición de la fracción en la columna

def buscar_fraccion(lst, f):
    #Función que retorna el índice de la posición de una fracción si la encuentra en la lista
    #En caso contrario retorna -1
    pos = -1
    for j in range(len(lst)):
        if ((lst[j].get_num() == f.get_num()) and (lst[j].get_denom() == f.get_denom())):
            pos = j
            break

    return pos
    
def imprimir_estado(valor):
    # Función que imprime la salida 
    salida.write("\n") 
    
def main():
    
    global matriz # Para trabajar con variables globales
    global salida
    
    arg_valido = True 

    if (len(sys.argv) == 3): #Si el número de argumentos es igual a 3
        arg_valido = False # No se intentará resolver el problema del archivo
        
        if (not(isinstance(sys.argv[1], str) and isinstance(sys.argv[2], str))): #Chequear tipos de argumento de línea de comandos
            print("\nTipo equivocado de argumentos (Se requiere: string string string)\n")

        if (sys.argv[1] != "-h"): #De estar presente, ejecutar argumento -h
            print("Argumento #2 debe ser '-h'\n")
            
        else:
            manual()

    if (len(sys.argv) == 2): #Si el número de argumentos es igual a 2
    
        if (not(isinstance(sys.argv[1], str))):
            print("\nTipo equivocado de argumentos (Se requiere: string string)\n") #Chequear tipos de argumento de línea de comandos
            arg_valido = False # Tipos equivocados 

        if (sys.argv[1] == "-h"): #De estar presente, ejecutar argumento -h
           arg_valido = False # Mostrar help
           manual()         

    if (len(sys.argv) > 3 or len(sys.argv) < 2):    
        print("\nNúmero equivocado de argumentos (se requieren 2 o 3)\n")
        arg_valido = False # Número equivocado de argumentos
    
        if (len(sys.argv) == 1): # Si no se agregaron argumentos además del nombre del programa
            print("Sólo se recibió el nombre del programa\n")
    
    if (arg_valido): #El número y tipo de los argumentos es válido
       lineas = []
       try:
           entrada = open(sys.argv[1],"r")        
           lineas = entrada.readlines() # Obtiene todas las líneas del archivo de entrada        
       except IOError:
          print ("\nError: No se logró encontrar el archivo\n")
       else:
          print ("\nDatos extraídos exitosamente del archivo\n")
          entrada.close()
        
       for i in range(len(lineas)): # Quitar comillas de las lineas
           lineas[i] = lineas[i].split(',')
            
#        variables_problema = int(lineas[0][2]) # Obtener el número de las variables del problema

    #Imprimir datos de línea de comandos
    n = len(sys.argv) 
    print("Total de argumentos pasados:", n) 
  
    print("\nArgumentos pasados:", end = " ") 
    for i in range(0, n): 
        print(sys.argv[i], end = " ")
    print("\n")


if __name__ == "__main__":
    main()
