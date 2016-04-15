import sqlite3
d = (
    ('VIZ', 10000),
    ('Centr', 20000),
    ('Uralmash', 15000),
    ('Elmash', 14000),
    ('Sortirovka', 7000)
)

con = sqlite3.connect("cat.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS distr")
cur.execute("CREATE TABLE distr (id INTEGER PRIMARY KEY , name TEXT, population INT)")
cur.executemany("INSERT INTO distr(name, population) VALUES (?,?)", d)
#except sqlite3.DatabaseError:
#    print ("Ошибка:")
#else:
#    print ("Запрос успешно выполнен")
con.commit()

with con:    
   # cur = con.cursor()    
    cur.execute("SELECT * FROM distr")
    rows = cur.fetchall()
 
    for row in rows:
        print (row)
        
cur.close()
con.close()
