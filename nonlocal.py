#!/usr/bin/env python
def func_outer():
    x = 2
    print( ' x равно' , x)
    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print( ' Локальное x сменилось на' , x)
func_outer()
#print( ' Глобальное x сменилось на' , x)
#если сменить nonlocal на global, то последняя запись пригодится для исполнения и понимания