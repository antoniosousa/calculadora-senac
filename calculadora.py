def somar(a,b):
    return a+b

def subtrair(a, b):
    return a-b

def dividir(a, b):
    return a/b

def multiplicar(a, b):
    return a*b
import math
num = float(input("Entre com um número:\n"))
raiz = math.sqrt(num)
print(f'\nA raiz quadrada de {num} é {raiz}\n')

while True:
    operacao = input(" 1-Somar \n 2-Dividir \n 3-Multiplicar \n 4-Subtrair \n 0-Sair \n Qual operação deseja: ")
    
    if int(operacao) == 0:
        break

    primeiro_numero = int(input("Primeiro numero: "))
    segundo_numero = int(input("Segundo numero: "))

    if int(operacao) == 1:
        resultado = somar(primeiro_numero, segundo_numero)
    elif int(operacao) == 2:
        resultado = dividir(primeiro_numero, segundo_numero)
    elif int(operacao) == 3:
        resultado = multiplicar(primeiro_numero, segundo_numero)
    print("Resultado: ",resultado,"\n")

