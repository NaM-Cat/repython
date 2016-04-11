import sys
import os; print(os.getcwd())
print( ' Аргументы командной строки: ' )
for i in sys. argv:
    print(i)
print( ' \n\nПеременная PYTHONPATH содержит' , sys. path, ' \n' )
print( __name__ )
if __name__ == '__main__' :
    print( ' Эта программа запущена сама по себе. ' )
else:
    print( ' Меня импортировали в другой модуль. ' )