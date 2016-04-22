#!/usr/bin/env python
import numpy.random as rand_prb
import calendar
import sqlite3
from datetime import date

LIST_OF_RECRUTED = []   #Список принятых на работу
LIST_OF_FIRED = []      #Список уволенных с работы
DISTRICTS = []          #Список районов

PRDCT_PERM = 2000               #количество зарабатываемое в день не зависимо от района города
PRDCT_DISTR = 1000              #количество зарабатываемое в день на 1000 жителей в зависимости от района
PRB_LIST = [0.17, 0.23, 0.6]    #вероятностное распределение на получение прибыли указанное в PRDCT_LIST
PRDCT_LIST = [1200, 1000, 800]  #список количества зарабатываемого в день с 1000 жителей с распределение вероятностей PRB_LIST

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
        #print_table(cur,"SELECT * FROM distr")
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
        print_table(cur,"SELECT * FROM distr")
        cur.close()
        con.close()


class Employee:
    """ Класс всех сотрудников"""
    
    def __init__(self, name, job):
        self.name = name
        self.job = job

class Papperboy(Employee):
    """ Разносчики газет
        Параметр type_productivity определяет вид производительности труда разносчика газет:
            1 - зарабатывает PRDCT_DISTR руб. в день на каждую 1000 жителей в районе
            2 - забаратывает PRDCT_PERM руб. в независимости от района города
            3 - зарабатывает сумму в PRDCT_LIST по вероятностному распределению PRB_LIST
                на каждую 1000 жителей в районе"""
    
    def __init__(self, name, type_productivity):
        
        Employee.__init__(self, name, 'papperboy')
        self.type_productivity = type_productivity
        print ('Добавляем Разносчика газет:', self.name, self.job, self.type_productivity)
        LIST_OF_RECRUTED.append(self)
    
        con = sqlite3.connect("catalog_zadach.db")
        cur = con.cursor()
        cur.execute("INSERT INTO employ(name, job, productivity) VALUES (?,?,?)",
                    (self.name,
                     self.job,
                     self.type_productivity))
        con.commit()
        #print_table(cur,"SELECT * FROM employ")      
        cur.close()
        con.close()
    
    def __str__(self):
        return '[Employee: %s, %s, %s]' % (self.name, self.job, self.type_productivity)
    
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%s|%s|%s" % (self.name, self.job, self.type_productivity)
        
    def __del__(self):
        LIST_OF_FIRED.append(self)
        LIST_OF_RECRUTED.remove(self)
        
    def prdct_perm(x):
        return x
    
def print_table(cursor, cmd):
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def productivity(perm = 0, distr = None, prb = False):
    if perm > 0 and distr == None and prb == False:
        return perm
    elif distr != None and perm == 0 and prb == False:
        return PRDCT_DISTR*(distr.population/1000)
    elif prb == True and perm == 0 and distr != None:
        return rand_prb.choice(PRDCT_LIST, p=PRB_LIST)*(distr.population/1000)
    else:
        print ('Введены некорретные параметры')
        return

def index_max_popul_distr(list_of_distr):
    index = 0
    for i in range(0,len(list_of_distr)-1):
        if(list_of_distr[i].population >= list_of_distr[i+1].population):
            index = i
    return index

def index_min_popul_distr(list_of_distr):
    index = 0
    for i in range(0,len(list_of_distr)-1):
        if(list_of_distr[i].population < list_of_distr[i+1].population):
            index = i
    return index   

def create_graphic(month, list_of_employ, list_of_distr):
    employ = 0
    con = sqlite3.connect("catalog_zadach.db")
    cur = con.cursor()
    for day in range(1,calendar.monthrange(2016,month)[1]+1):
        for distr in range(0,len(list_of_distr)):
            if employ == len(list_of_employ):
                employ = 0
            cur.execute("INSERT INTO graphic(date, employ_name, distr_name) VALUES (?,?,?)",
                        (date(2016,month,day),
                        list_of_employ[employ].name,
                        list_of_distr[distr].name))
            employ += 1
    con.commit()
 #   print_table(cur,"SELECT * FROM graphic")
    cur.close()
    con.close()

def change_graphic(date, employ_name, distr_name):
    con = sqlite3.connect("catalog_zadach.db")
    cur = con.cursor()
    cur.execute("UPDATE graphic SET employ_name = (?) WHERE distr_name = (?) and date = (?)",
                (employ_name, distr_name, date))
    con.commit()
  #  print_table(cur,"SELECT * FROM graphic")
    cur.close()
    con.close()

def calc_income(start_date, finish_date):
    total_productivity = 0
    for day in range(start_date.__getattribute__('day'), finish_date.__getattribute__('day')):
        
    

con = sqlite3.connect("catalog_zadach.db")
cur = con.cursor()
try:
    cur.execute("DROP TABLE IF EXISTS distr")
    cur.execute("CREATE TABLE distr (id INTEGER PRIMARY KEY , name TEXT, population INTEGER)")
    cur.execute("DROP TABLE IF EXISTS employ")
    cur.execute("CREATE TABLE employ (id INTEGER PRIMARY KEY , name TEXT, job TEXT, productivity INTEGER)")
    cur.execute("DROP TABLE IF EXISTS graphic")
    cur.execute("CREATE TABLE graphic (date DATE, employ_name TEXT, distr_name TEXT)")
except sqlite3.DatabaseError:
    print ("Ошибка в базе данных!!!!!!!!!!!!!!!")
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

Papperboy('Алексеев Геннадий Викторович',1)
Papperboy('Хазанов Владимир Андреевич',2)
Papperboy('Олейко Иван Петрович',3)

print('--------------------')

#LIST_OF_RECRUTED[0].productivity = prdct_perm
#LIST_OF_RECRUTED[1].productivity = prdct_prb
#LIST_OF_RECRUTED[2].productivity = prdct_distr(DISTRICTS[3])

print('--------------------')

Calendar = calendar.TextCalendar()
print(Calendar.formatmonth(2016,4))

print('--------------------')
print(date(2016,4,11))
try:
    d=date(2016,2,28).__getattribute__('day')
except ValueError or SyntaxError:
    pass
print(d)

print('--------AAAAAAAAA------------')

create_graphic(4,LIST_OF_RECRUTED,DISTRICTS)

print('--------AAAAAAAAA------------')

change_graphic(date(2016,4,1),'Алексеев Геннадий Викторович','Centr')

print('--------AAAAAAAAA------------')

con = sqlite3.connect("catalog_zadach.db")
cur = con.cursor()
cur.execute("SELECT * FROM graphic")
rows = cur.fetchall()

print(rows[0][2])
print(productivity(prb = True))



    
    
    