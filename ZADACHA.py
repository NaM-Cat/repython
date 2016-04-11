#!/usr/bin/env python
import numpy.random as rand_prb
import calendar
from datetime import date

LIST_OF_RECRUTED = []   #Список принятых на работу
LIST_OF_FIRED = []      #Список уволенных с работы
DISTRICTS = []          #Список районов

class District:
    """Районы города"""
    
    def __init__(self, name, population):
        self.name = name
        self.population = population
        DISTRICTS.append(self) 


class Employee:
    """ Класс всех сотрудников"""
    
    def __init__(self, name):
        self.name = name

class Papperboy(Employee):
    """ Разносчики газет"""
    
    def __init__(self, name, productivity = 0):
        Employee.__init__(self, name)
        LIST_OF_RECRUTED.append(self)
        self.productivity = productivity
    
    def __del__(self):
        LIST_OF_FIRED.append(self)
        LIST_OF_RECRUTED.remove(self)
        
        
   
def prdct_perm():
    return 2000

def prdct_distr(district):
    return 1000*(district.population/1000)

def prdct_prb():
    prb_list = [0.17, 0.23, 0.6]
    prdct_list = [1200, 1000, 800]
    return rand_prb.choice(prdct_list, p=prb_list)

District('VIZ', 10000)
District('Centr', 20000)
District('Uralmash', 15000)
District('Elmash', 14000)
District('Sortirovka', 7000)

print (DISTRICTS[0].name, DISTRICTS[0].population)

print('--------------------')


Papperboy('Алексеев Геннадий Викторович')
Papperboy('Хазанов Владимир Андреевич')
Papperboy('Олейко Иван Петрович')

print(LIST_OF_RECRUTED[1].name)

print('--------------------')

LIST_OF_RECRUTED[0].productivity = prdct_perm
LIST_OF_RECRUTED[1].productivity = prdct_prb
LIST_OF_RECRUTED[2].productivity = prdct_distr(DISTRICTS[3])

print (LIST_OF_RECRUTED[2].productivity)

print('--------------------')

Calendar = calendar.TextCalendar()
print(Calendar.formatmonth(2016,4))

print('--------------------')
print(date(2016,4,11))

print('--------------------')
a = 1
a = 'day'
print(a)


    
    
    