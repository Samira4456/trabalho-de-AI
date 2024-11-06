# trabalho-de-AI
#calculadora

#Funçao para soma
def adicionar(x, y):
    return x + y

#Funçao para subtraçao
def subtrair(x, y):
    return x - y

#Funçao para multiplicaçao
def multiplicar(x, y):
    return x * y

#Funçao para dividir
def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

#criando uma lista
minha_lista = [1,2,3,4 ]
print(minha_lista)

ultimo_elemento = minha_lista.pop()
print(ultimo_elemento)
print(minha_lista)
