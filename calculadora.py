#Funçao para soma
def soma (x, y):
    return x+y

#Funçao principal
def parameter(num1, num2):
    pass

def calculadora ():
    num1 = int(input( "primeiro num: "))
    num2 = int(input( "Segundo num: "))
    operador=input("Digite a operacao: ")

    if operador == "soma":
        result= soma(num1, num2)
        print ("Resultado: " + str(result))
    elif operador == "multipli":
        print("resultado da multipli")
        var = num1,* num2
    else:
        print("operador invalido")

#Executa a calculadora
calculadora()

