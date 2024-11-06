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


while True:
    escolha = input("Digite a escolha (1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {adicionar(num1, num2)}")

        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")

        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")

        proxima_calculacao = input("Deseja fazer outra operação? (sim/não): ")
        if proxima_calculacao.lower() != 'sim':
            break
    else:
        print("Entradainválida")
