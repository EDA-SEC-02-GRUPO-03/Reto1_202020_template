"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import shellsort as sh
from Sorting import selectionsort as sel 
from Sorting import insertionsort as ins 
from time import process_time 


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1



def loadCSVFile (file1,file2, sep=";"):
    lst1 = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst1 = lt.newList() #Usando implementacion linkedlist
    lst2 = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst2 = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivos ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file1, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst1,row)
        with open(file2, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst2,row)

    except:
        print("Hubo un error con la carga de los archivos")

    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return (lst1,lst2) 

def req1(lst1, lst2, criteria1, column1, criteria2, column2):

    if lst1['size'] == 0 or lst2['size'] == 0:
        print ('Lista vacía')
    else:
        t1_start = process_time()
        counter = 0
        iterator1 = it.newIterator(lst1)
        i = 0
        positions = []
        while  it.hasNext(iterator1):
            element = it.next(iterator1)
            if criteria1.lower() in element[column1].lower(): #filtrar por palabra clave 
                positions.append(i)
            i+=1
        for i in positions:
            element = lt.getElement(lst2 ,i)
            if float(element[column2]) >= float(criteria2):
                counter += 1            
    t1_stop = process_time()
    print('EL tiempo es de ', t1_stop-t1_start, ' segundos')
    return counter

def req2 (lst, function, criteria, n):
    
    t1_start = process_time()
    result = lt.newList('ARRAY_LIST')
    nombres = lt.newList('ARRAY_LIST')
    votos = lt.newList('ARRAY_LIST')
    sh.shellSort(lst, function, criteria)
    #sel.selectionSort(lst, function, criteria)       
    #ins.insertionSort(lst,function,criteria)

    for i in range(n+1):
        lt.addLast(result,lt.getElement(lst, i))    
    iterator=it.newIterator(result)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        lt.addLast(nombres, element['title'])
        lt.addLast(votos, element[criteria])
    final = lt.newList('ARRAY_LIST')
    for i in range(n+1):
        lt.addLast(final, (lt.getElement(nombres, i),lt.getElement(votos,i)))
    lt.addLast(final, lt.getElement(final, 0))
    lt.removeFirst(final)
    lt.removeFirst(final)
    t1_stop = process_time()
    print('El tiempo fue de ', t1_stop-t1_start, ' segundos')
    return final

def loadMovies ():
    lst = loadCSVFile("theMoviesdb/movies-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """

    listaD = lt.newList()   # lista de detalles
    listaC = lt.newList()   # lista de detalles
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                datos = loadCSVFile("Data\AllMoviesDetailsCleaned.csv","Data\AllMoviesCastingRaw.csv") 
                listaD = datos[0]
                listaC = datos[1]
                print("Datos de detalles cargados, ",listaD['size']," elementos cargados")
                print("Datos de casting cargados, ",listaC['size']," elementos cargados")    

            elif int(inputs[0])==2: #opcion 2
               

            elif int(inputs[0])==3: #opcion 3
                

            elif int(inputs[0])==4: #opcion 4
                

            elif int(inputs[0])==5: #opcion 5
                

            elif int(inputs[0])==6: #opcion 6
               


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()