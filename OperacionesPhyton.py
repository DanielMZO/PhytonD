a = int(input("Enter First Number: "))

b = int(input("Enter second Number: "))
operador = input ("Enter a operator: ")

type(a)
type(b)
type(operador)

# realizar una suma de 2 numeros
def suma():
    resultado = a + b
    print (resultado)
# restar 10 - 3 = 7
def resta():
    resultado = a - b
    print (resultado)

# multiplicacion de 10*3 = 30
def multiplicacion():
    resultado = a * b
    print (resultado)

# division natural resultado = 10/3 que es aprox 3.333
def division():
    resultado = a / b
    print (resultado)

# division con floor/piso, el resultado se redondea hacia abajo
def divisionFloor():
    resultado = a // b  # resultado = 3, no 3.3333
    print (resultado)

# modulo/residuo, el residuo de una division
def mod():
    resultado = a % b  # resultado es 1
    print (resultado)

# exponencial, eleva a la potencia de
def expo():
    resultado = a ** b  # 10 elevado a 3 = 1000
    print (resultado)

if operador == "+":
    suma()
elif operador == "-":
    resta()
elif operador == "*":
    multiplicacion()
elif operador == "/":
    division()
elif operador == "//":
    divisionFloor()
elif operador == "**":
    expo()
else: print ("invalid operator")
