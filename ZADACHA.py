#!/usr/bin/env python
import numpy.random as rand_prb

LIST_OF_RECRUTED = []   #Список принятых на работу
LIST_OF_FIRED = []      #Список уволенных с работы
DISTRICTS = []          #Список районов

class District:
    """Районы города"""
    
    def __init__(self, name, population):
        self.name = name
        self.population = population


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
        
        
   # def recruit(self, name)
   #     Papperboy.__init__(self, name);
   
def prdct_perm():
    return 2000

def prdct_distr(district):
    return 1000*(district.population/1000)

def prdct_prb():
    prb_list = [0.17, 0.23, 0.6]
    prdct_list = [1200, 1000, 800]
    return rand_prb.choice(prdct_list, p=prb_list)

DISTRICTS.append(District('VIZ', 10000))
DISTRICTS.append(District('Centr', 20000))
DISTRICTS.append(District('Uralmash', 15000))
DISTRICTS.append(District('Elmash', 14000))
DISTRICTS.append(District('Sortirovka', 7000))
print (DISTRICTS[0].name, DISTRICTS[0].population)
#print(DISTRICTS)
print('--------------------')

Workers = []
Workers.append(Papperboy('Алексеев Геннадий Викторович'))
Workers.append(Papperboy('Хазанов Владимир Андреевич'))
Workers.append(Papperboy('Олейко Иван Петрович'))
#print(Workers)
print('--------------------')

Workers[0].productivity = prdct_perm
Workers[1].productivity = prdct_prb
Workers[2].productivity = prdct_distr(DISTRICTS[3])
print (Workers[2].productivity)

#print(Workers)

#print(Workers)
print('--------------------')



    
    
    