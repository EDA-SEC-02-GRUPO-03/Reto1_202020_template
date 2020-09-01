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
    print('1- Cargar Datos')
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("7- Mostrar datos por director")
    print("0- Salir")

def lessfunction(element1, element2, criteria):
    if float(element1[criteria]) < float(element2[criteria]):
        return True
    return False

def greaterfunction(element1, element2, criteria):
    if float(element1[criteria]) > float(element2[criteria]):
        return True
    return False

def compareRecordIds():
    pass

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


def req1 (lst1, lst2, criteria1, column1, criteria2, column2):

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

def req4(name, lst1, lst2):
    t1_start = process_time() #tiempo inicial
    counter = 0
    nPart = 0
    nombres = []
    directores = []
    sumProm = 0
    for i in range(1, lt.size(lst2)):
        counter += 1
        elemento = lt.getElement(lst2, i)
        actores = (elemento['actor1_name'] +
         elemento['actor2_name'] + elemento['actor3_name'] +
         elemento['actor4_name'] + elemento['actor5_name']).lower()
        if name.lower() in actores:
            nPart += 1
            nombres.append((lt.getElement(lst1, counter))['title'])
            directores.append(elemento['director_name'])
            sumProm += float((lt.getElement(lst1, counter))['vote_average'])
    if nPart == 0:
        print('\nActor no encontrado\n')
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos\n")
        pass
    else:
        prom = sumProm / nPart
        direct = 'Batman'
        for i in directores:
            if directores.count(i) >= directores.count(direct):
                direct = i
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return (nombres, nPart, round(prom, 1), direct)

def req5(lst, criteria1, column1, column2, column3):
    if lst['size'] == 0:
        print ('Lista vacía')
    else:
        t1_start = process_time()
        iterator1 = it.newIterator(lst)
        nombres = lt.newList('ARRAY_LIST')
        votos = lt.newList('ARRAY_LIST')
        counter = 0
        while  it.hasNext(iterator1):
            element = it.next(iterator1)
            if criteria1.lower() in element[column1].lower(): #filtrar por palabra clave 
                lt.addLast(nombres, element[column2])
                lt.addLast(votos, element[column3])
                counter += 1
        suma = 0
        for i in range(lt.size(votos)):
            suma += float(lt.getElement(votos,i))
        t1_stop = process_time()
        tiempo = t1_stop-t1_start
        return nombres['elements'],counter,suma/lt.size(votos),tiempo

def req6 (lst1, criteria1, column1, function, criteriaf, n):        
    porgenero = lt.newList("ARRAY_LIST")
    iterator = it.newIterator(lst1)
    lt.addFirst(porgenero, '')
    while it.hasNext(iterator):
        element = it.next(iterator)
        if criteria1.lower() in element[column1].lower():
            lt.addLast(porgenero, element)
    lt.removeFirst(porgenero)
    listado = req2 (porgenero, function, criteriaf, n)
    return listado

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    listaD = lt.newList()   # se require usar lista definida
    listaC = lt.newList() 
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                datos = loadCSVFile("Data\\theMoviesdb\\AllMoviesDetailsCleaned.csv","Data\\theMoviesdb\\AllMoviesCastingRaw.csv") #llamar funcion cargar datos
                listaD = datos[0]
                listaC = datos[1]
                print("Datos de detalles cargados, ",listaD['size']," elementos cargados")
                print("Datos de casting cargados, ",listaC['size']," elementos cargados")    

            elif int(inputs[0])==2: #opcion 2
                gb1 = int(input('Más Votos (1) o Menos Votos (0):\n'))
                n1 = int(input('¿Cuántas películas?\n'))
                gb2 = int(input('Mejor Promedio (1) o Peor Promedio (0):\n'))
                n2 = int(input('¿Cuántas películas?\n'))
                if gb1 == 1:
                    function1 = greaterfunction
                elif gb1 == 0:
                    function1 = lessfunction
                if gb2 == 1:
                    function2 = greaterfunction
                elif gb2 == 0: 
                    function2 = lessfunction
                resultados1 = req2(listaD, function1, 'vote_count', n1)
                resultados2 = req2(listaD, function2, 'vote_average', n2)
                print('Por votos:\n',resultados1 )
                print('Por promedio:\n', resultados2)

            elif int(inputs[0])==3: #opcion 3
                pass

            elif int(inputs[0])==4: #opcion 4
                if listaD==None or listaD['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    name = input('\nIngrese el nombre del actor a consultar:\n')
                    result = req4(name, listaD, listaC)
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
                        
            elif int(inputs[0])==5: #opcion 5
                genero = input('Ingrese el género:\n')
                resultado = req5(listaD, genero, 'genres', 'title', 'vote_average' )
                print ('Las películas de ', genero, 'son:\n', resultado[0])
                print ('Hay ', resultado[1], ' películas de ', genero)
                print('El promedio de votación es de ', resultado[2])
                print('El tiempo fue de ', resultado[3], ' segundos')

            elif int(inputs[0])==6: #opcion 6
                genero = input('Ingrese el género:\n')
                gb1 = int(input('Más Votos (1) o Menos Votos (0):\n'))
                n1 = int(input('¿Cuántas películas?\n'))
                gb2 = int(input('Mejor Promedio (1) o Peor Promedio (0):\n'))
                n2 = int(input('¿Cuántas películas?\n'))
                if gb1 == 1:
                    function1 = greaterfunction
                elif gb1 == 0:
                    function1 = lessfunction
                if gb2 == 1:
                    function2 = greaterfunction
                elif gb2 == 0: 
                    function2 = lessfunction
                resultado1 = req6(listaD, genero, 'genres', function1, 'vote_count', n1)
                resultado2 = req6(listaD, genero, 'genres', function2, 'vote_average', n2)
                print('Por votos:\n',resultado1 )
                print('Por promedio:\n', resultado2)

            elif int(inputs[0])==7: #opcion 7
                director = input('Ingrese el nombre del director:\n')
                pelis = req1(listaC, listaD, director, 'director_name', 6, 'vote_average')
                print('El director ', director, ' tiene ', pelis, ' películas buenas.')

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

                
if __name__ == "__main__":
    main()