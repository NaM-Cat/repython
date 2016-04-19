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
        DISTRICTS.append(self)
        print ('Добавляем район:', self.name)
        con = sqlite3.connect("catalog_zadach.db")
        cur = con.cursor()
        cur.execute("INSERT INTO distr(name, population) VALUES (?,?)", (self.name, self.population))
        con.commit()
        cur.execute("SELECT * FROM distr")
        print (cur.fetchall())
        cur.close()
        con.close()

    def __str__(self):
        return '[District: %s, %s]' % (self.name, self.population)
    
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%s|%s" % (self.name, self.population)
    
    def change_population(self, new_population):
        self.population = new_population
        print ('Изменяем численность района:', self.name)
        con = sqlite3.connect("catalog_zadach.db")
        cur = con.cursor()
        cur.execute("UPDATE distr SET population = (?) WHERE name = (?)", (new_population, self.name))
        con.commit()
        cur.execute("SELECT * FROM distr")
        print (cur.fetchall())
        cur.close()
        con.close()


class Employee:
    """ Класс всех сотрудников"""
    
    def __init__(self, name, job):
        self.name = name
        self.job = job

class Papperboy(Employee):
    """ Разносчики газет"""
    
    def __init__(self, name, productivity = 0):
        
        Employee.__init__(self, name, 'papperboy')
        self.productivity = productivity
        print ('Добавляем Разносчика газет:', self.name)
        LIST_OF_RECRUTED.append(self)
    
        con = sqlite3.connect("catalog_zadach.db")
        cur = con.cursor()
        cur.execute("INSERT INTO employ(name, job, productivity) VALUES (?,?,?)",
                    (self.name,
                     self.job,
                     self.productivity))
        con.commit()
        cur.execute("SELECT * FROM employ")
        print (cur.fetchall())
        cur.close()
        con.close()
    
    def __str__(self):
        return '[Employee: %s, %s, %s]' % (self.name, self.job, self.productivity)
    
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%s|%s|%s" % (self.name, self.job, self.productivity)
        
    def __del__(self):
        LIST_OF_FIRED.append(self)
        LIST_OF_RECRUTED.remove(self)
        
    def prdct_perm(x):
        return x
   
def prdct_distr(district):
    return 1000*(district.population/1000)

def prdct_prb():
    prb_list = [0.17, 0.23, 0.6]
    prdct_list = [1200, 1000, 800]
    return rand_prb.choice(prdct_list, p=prb_list)

con = sqlite3.connect("catalog_zadach.db")
cur = con.cursor()
try:
    cur.execute("DROP TABLE IF EXISTS distr")
    cur.execute("CREATE TABLE distr (id INTEGER PRIMARY KEY , name TEXT, population INTEGER)")
    cur.execute("DROP TABLE IF EXISTS employ")
    cur.execute("CREATE TABLE employ (id INTEGER PRIMARY KEY , name TEXT, job TEXT, productivity INTEGER)")
except sqlite3.DatabaseError:
    print ("Ошибка:")
else:
    print ("Запрос успешно выполнен")
con.commit()
cur.close()
con.close()

District('VIZ', 10000)
District('Centr', 20000)
District('Uralmash', 15000)
District('Elmash', 14000)
District('Sortirovka', 7000)

print('--------------------')

DISTRICTS[0].change_population(11000)

print('--------------------')

Papperboy('Алексеев Геннадий Викторович',Papperboy.prdct_perm(2000))
Papperboy('Хазанов Владимир Андреевич')
Papperboy('Олейко Иван Петрович')

print('--------------------')

#LIST_OF_RECRUTED[0].productivity = prdct_perm
#LIST_OF_RECRUTED[1].productivity = prdct_prb
#LIST_OF_RECRUTED[2].productivity = prdct_distr(DISTRICTS[3])

print('--------------------')

Calendar = calendar.TextCalendar()
print(Calendar.formatmonth(2016,4))

print('--------------------')
print(date(2016,4,11))

print('--------------------')
a = 1
a = 'day'
print(a)


    
    
    