""" Funciones/metodos """
def mensaje():
    print("Utilizando funciones")
    print("Impresión de un mensaje por función")

mensaje()

""" Funciones/metodos sin parametros"""
def suma():
    num1=46
    num2=85
    print(num1+num2)
suma() 

""" Funciones/metodos con parametros, reutilizando codigo en 2da y 3ra llamda"""
def multiplicacion(num01,num02):
    print(num01*num02)
multiplicacion(9,3)

multiplicacion(12,5)
multiplicacion(4,8)

""" Funciones/metodos que devuelve un valor"""
def division(num1,num2):
    resultado=num1/num2
    return resultado
almacena_valor=division(1500,10)
print(almacena_valor)
"""print(division(1500,5)) """ #Otra forma de imprimir la función
