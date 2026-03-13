#Exercício 1
"""
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
"""

#Exercício 2

"""
soma = 0
for i in range(6):
    numero = int (input("Digite um número inteiro: "))
if numero % 2 == 0:
        soma += numero
print("A soma dos números pares é:", soma)
"""


#Exercício 3

"""
from random import randint

numero = randint(0, 10)
tentativas = 0

while True:
    chute = int (input("Tente adivinhar o número (0 e 10): "))
    tentativas += 1
    
    if chute < numero:
        print("Mais alto...")
    elif chute > numero:
        print("Mais baixo...")
    else:
        print("Acertou!")
        print("Número de tentativas:", tentativas)
        break
"""

#Exercício 4
"""
soma = 0
contador = 0

while True:
    numero = int (input("Digite um número (999): "))
    
    if numero == 999:
        break
    
    soma += numero
    contador += 1

soma += numero
contador += 1

print("Quantidade de números digitados:", contador)
print("Soma dos números digitados:", soma)
"""

#Exercício 5
"""
while True:
    numero = int (input("Digite um número inteiro para ver a tabuada: "))
    
    if numero < 0:
        
        break
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        """
        
#Exercício 6
"""
frase = input("Digite uma frase: ").upper().replace(" ", "")

invertida = frase[::-1]

if frase == invertida:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
"""

#Exercício 7
"""     
maior18= 0
homens= 0
mulheres20 = 0

while True:
    idade = int (input("Digite a idade da pessoa: "))
    
    if idade < 0:
        break
    
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
    
    if idade > 18:
        maior18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres20 += 1
    
    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar == "N":
        break
    
print("Quantidade de pessoas maiores de 18 anos:", maior18)
print("Quantidade de homens:", homens)
print("Quantidade de mulheres com menos de 20 anos:", mulheres20)
"""
    
    
        
        
        
        
