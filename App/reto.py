"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los 
 *Andes 
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
  Este módulo es una aplicación básica con un menú de opciones para cargar 
  datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import selectionsort as sort

from time import process_time 

def less(element1, element2):
    if float(element1['vote_average']) < float(element2['vote_average']):
        return True
    return False

def greater(element1, element2):
    if float(element1['vote_average']) > float(element2['vote_average']):
        return True
    return False

def loadCSVFile (file1, file2, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro,
        si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst1 = lt.newList() #Usando implementacion linkedlist
    #lst2 = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst2 = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
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
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst1, lst2


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Clasificar peliculas por votación")
    print("6- Consultar la información de un actor")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio
            definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower():  
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una 
    columna dada
    """
    t1_start = process_time() #tiempo inicial
    counter = 0
    for i in lst:
        if criteria in i[column]:
            counter += 1
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el 
    criterio
    """
    NewList = None
    NewList = lt.newList("ARRAY_LIST")
    t1_start = process_time() #tiempo inicial
    sort.selectionSort(lst, function)
    for i in range(elements+1):
        lt.addFirst(NewList, lt.getElement(lst, i))
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos\n")
    return NewList

def ActorData(name, lst1, lst2):
    t1_start = process_time() #tiempo inicial
    counter = 0
    nPart = 0
    nombres = []
    directores = []
    sumProm = 0
    for i in range(lt.size(lst2)):
        counter += 1
        elemento = lt.getElement(lst2, i)
        actores = (elemento['actor1_name'] +
         elemento['actor2_name'] + elemento['actor3_name'] +
         elemento['actor4_name'] + elemento['actor5_name']).lower().replace(' ','')
        if name.lower() in actores:
            nPart += 1
            nombres.append((lt.getElement(lst1, counter))['title'])
            directores.append(elemento['director_name'])
            sumProm += float((lt.getElement(lst1, counter))['vote_average'])
    if nPart == 0:
        print('\nActor no encontrado\n')
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos\n")
    else:
        prom = sumProm / nPart
        direct = 'Batman'
        for i in directores:
            if directores.count(i) >= directores.count(direct):
                direct = i
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return (nombres, nPart, round(prom, 1), direct)

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos
    adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde
    el archivo
    Args: None
    Return: None 
    """
    lista1 = lt.newList()   # se require usar lista definida
    lista2 = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                # lista1, lista2 = loadCSVFile("Data/theMoviesdb/AllMoviesDetailsCleaned.csv", "Data/theMoviesdb/AllMoviesCastingRaw.csv")
                lista1, lista2 = loadCSVFile("Data/theMoviesdb/SmallMoviesDetailsCleaned.csv", "Data/theMoviesdb/MoviesCastingRaw-small.csv")
                # lista1, lista2 = loadCSVFile("Data/theMoviesdb/short.csv", "Data/theMoviesdb/shortcasting.csv")
                print("Datos cargados, ",lista1['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista1['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista1) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista1)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria2 = input('\nIngrese 0 para las de mayor cantidad de votos o 1 para las de menor cantidad:\n')
                    cant2 = input('\nIngrese la cantidad de películas que desea ver por por la cantidad de votos:\n')
                    if int(criteria2[0]) == 0:
                        count = orderElementsByCriteria(greater, 'vote_count', lista1, int(cant2))
                    elif int(criteria2[0]) == 1:
                        count = orderElementsByCriteria(less, 'vote_count', lista1, int(cant2))
                    print('\nLos resultados por cantidad de votos son:')
                    print('-' * 30)
                    for i in range(1, len(count['elements'])):
                        data = lt.getElement(count, i)
                        print(data['title'], data['vote_count'])

                    criteria1 = input('\nIngrese 0 para las de mayor promedio o 1 para las de menor promedio:\n')
                    cant1 = input('\nIngrese la cantidad de películas que desea ver por por el promedio de calificación:\n')
                    try:
                        if int(criteria1[0]) == 0:
                            prom = orderElementsByCriteria(greater, 'vote_average', lista1, int(cant1))
                        elif int(criteria1[0]) == 1:
                            prom = orderElementsByCriteria(less, 'vote_average', lista1, int(cant1))
                        print('\nLos resultados por promedio son:')
                        print('-' * 30)
                        for i in range(1, len(prom['elements'])):
                            data = lt.getElement(prom, i)
                            print(data['title'], data['vote_average'])
                    except:
                        print('Ha ocurrido un error al ingresar los parametros')
            elif int(inputs[0])==6: #opcion 6
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    name = input('\nIngrese el nombre del actor a consultar:\n')
                    result = ActorData(name, lista1, lista2)
                    if result[1] == 0:
                        pass
                    else:
                        print('Las películas en las que ha participado')
                        print('-' * 40)
                        for i in result[0]:
                            print('-',i)
                        print('\n', name, 'ha participado en', result[1], 'peliculas')
                        print('El promedio de las películas es:', result[2])
                        print('El director con quien más ha colaborado es:', result[3])
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()