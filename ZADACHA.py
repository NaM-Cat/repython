#!/usr/bin/env python
import numpy.random as rand_prb
import calendar
import sqlite3
from datetime import date

LIST_OF_RECRUTED = []   #Список принятых на работу
LIST_OF_FIRED = []      #Список уволенных с работы
DISTRICTS = []          #Список районов

class District:
    """Районы города"""
    
    def __init__(self, name, population):
        self.name = name
        self.population = population
        DISTRICTS.append((self.name, self.population))

    def __str__(self):
        return '[District: %s, %s]' % (self.name, self.population)
    
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%s|%s" % (self.name, self.population)


class Employee:
    """ Класс всех сотрудников"""
    
    def __init__(self, name, job):
        self.name = name

class Papperboy(Employee):
    """ Разносчики газет"""
    
    def __init__(self, name, productivity = 0):
        Employee.__init__(self, name, 'papperboy')
        LIST_OF_RECRUTED.append(name, productivity, Employee.__init__.job)
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

con = sqlite3.connect("catalog_zadach.db")
cur = con.cursor()
try:
    cur.execute("DROP TABLE IF EXISTS distr")
    cur.execute("CREATE TABLE distr (id INTEGER PRIMARY KEY , name TEXT, population INTEGER)")
    cur.executemany("INSERT INTO distr(name, population) VALUES (?,?)", DISTRICTS)
except sqlite3.DatabaseError:
    print ("Ошибка:")
else:
    print ("Запрос успешно выполнен")
con.commit()
cur.close()
con.close()
#raw_input()

print (DISTRICTS)

print('--------------------')


#Papperboy('Алексеев Геннадий Викторович')
#Papperboy('Хазанов Владимир Андреевич')
#Papperboy('Олейко Иван Петрович')

#print(LIST_OF_RECRUTED[1].name)

print('--------------------')

#LIST_OF_RECRUTED[0].productivity = prdct_perm
#LIST_OF_RECRUTED[1].productivity = prdct_prb
#LIST_OF_RECRUTED[2].productivity = prdct_distr(DISTRICTS[3])

#print (LIST_OF_RECRUTED[2].productivity)

print('--------------------')

Calendar = calendar.TextCalendar()
print(Calendar.formatmonth(2016,4))

print('--------------------')
print(date(2016,4,11))

print('--------------------')
a = 1
a = 'day'
print(a)


    
    
    