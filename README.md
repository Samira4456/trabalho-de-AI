# trabalho-de-AI
#Calculadora
def calculadora():
    num1 = int(input("primeiro num: "))
    num2 = int(input("Segundo num: "))
    operador = input("Digite a operacao: " + ' *' "/ " " - ")

    #Funçao para soma
def soma (x, y):
    return x+y

#Funçao para multiplicacao
def multplicacao (x, y):
    return

#Funçao para dividi
def dividi (x, y ):
    return

#Funçao para subtracao
def subtracao (x, y):
    return

#Funçao principal
def parameter(num1, num2):
    pass

    if operador == "soma":
        result= soma(num1, num2)
        print ("Resultado: " + str(result))
    elif operador == "multipli":
        print("resultado da multipli")
        var = num1,* num2
    else:
        print("operador invalido")

    if  operador == "multplicacao":
        result= multplicacao(num1, num2)
        print("Resultado: " * str(result))
    elif operador == "multipli":
        print ("resultado da multplicaçao")
        var= num1,* num2

    if  operador == "dividi":
        result= dividi(num1, num2)
        print("Resultado: "/ str(result))
    elif operador == "dividi":
        print("resultado da dividi")
        var= num1, num2


    if  operador == "subtraçao":
        result= subtraçao(num1, num2)
        print("Resultado: " - str(result))
    elif operador == "subtraçao":
        print ("resultado da subtraçao")
        var= num1,- num2
#Executa a calculadora
calculadora()
