#Exercício 1

"""
import time

def contagem(n):
    if n ==0:
        print("Fogo!") 
    else:
        print(n)
        time.sleep(1)
        
        contagem(n - 1)
        
num = int(input("Digite um numero:"))
contagem(num)
"""

#Exercício 2

"""
def fatorial (n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * fatorial(n -1)
    
num = int(input("Digite um numero:"))
print("Fatorial:", fatorial(num))
"""

#Exercício 3

"""
def fib(n):
    if n == 1 or n == 2:
        return 1
    
    else:
        return (fib -1) + fib(n - 2)
n = int(input("Digite a posição do termo:"))
print("Termo de sequência:", fib(n))

"""

#Exercício 4

"""
def somar_lista(lista):
    if lista ==[]:
        return 0
    
    else:
        return lista[0] + somar_lista(lista[1:])
    
numeros = [2,4,6,8]
print("Soma da lista:", somar_lista(numeros))
"""
        
#Exercício 5

"""
def  potencial(base, expoente):
    if expoente == 0:
        
        return 1
    
    else:
        return base * potencia(base, expoente - 1)
b = int(input("Digite a base:"))
e = int(input("Digite um expoente:"))
print("Resultado:", (b, e))
"""
        
#Exercício 6
#função recursiva para inverter uma palavra
"""

def inverter(palavra):
    # Caso base
    if palavra == "":
        return ""
    
    else:
        return palavra[-1] + inverter(palavra[:-1])

texto = input("Digite uma palavra: ")
print("Invertida:", inverter(texto))
"""
#Exercício 7


"""
def inverter(palavra):

    if palavra == "":
        return ""
   
    else:
        return palavra[-1] + inverter(palavra[:-1])


texto = input("Digite uma palavra: ")
print("Invertida:", inverter(texto))
def inverter(palavra):
    # Caso base
    if palavra == "":
        return ""
    
    else:
        return palavra[-1] + inverter(palavra[:-1])


texto = input("Digite uma palavra: ")
print("Invertida:", inverter(texto))
def inverter(palavra):

    if palavra == "":
        return ""
    
    else:
        return palavra[-1] + inverter(palavra[:-1])

texto = input("Digite uma palavra: ")
print("Invertida:", inverter(texto))
def inverter(palavra):
    
    if palavra == "":
        return ""
    
    else:
        return palavra[-1] + inverter(palavra[:-1])


texto = input("Digite uma palavra: ")
print("Invertida:", inverter(texto))
def inverter(palavra):
    
    if palavra == "":
        return ""
    
    else:
        return palavra[-1] + inverter(palavra[:-1])


texto = input("Digite uma palavra: ")
print("Invertida:", inverter(texto))
"""



