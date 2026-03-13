#Exercício 1
"""
velocidade = float (input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    print("Multado! Você excedeu o limite de velocidade.")
    
else:    
    print("Velocidade dentro do limite. Boa viagem!")
    """
    
#Exercício 2

"""
numero = int (input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
"""

#Exercício 3

"""
n1 = float (input("Digite o primeiro número: "))
n2 = float (input("Digite o segundo número: "))
if n1 > n2:
    print("O número", n1, "é maior que", n2)
elif n2 > n1:
    print("O número", n2, "é maior que", n1)
    
else:
    print("Os números são iguais.")
"""
#Exercício 4

"""
distancia = float (input("Digite a distância percorrida em km: "))
if distancia <= 200:
    custo = distancia * 0.50
else:
    custo = distancia * 0.45
print("O custo da passagem é: R$", custo)
"""

#Exercício 5

"""
ano = int (input("Digite o ano de nascimento: "))
idade = 2025 - ano

if idade >= 12:
    print("Criança")
    
elif idade <= 17:
    print("Adolescente")
    
elif idade <= 64:
    print("Adulto")
else:
    print("Idoso") 
"""
#Exercício 6

"""
valor_casa = float (input("Digite o valor da casa: R$ "))
salario = float (input("Salário"))
anos = int (input("Quantos anos para pagar? "))

meses = anos * 12
prestacao = valor_casa / meses
if prestacao > salario * 0.30:
    print("Empréstimo negado. A prestação mensal é maior que 30% do salário.")
else:    print("Empréstimo aprovado. A prestação mensal é de R$", prestacao)
"""

#Exercício 7

"""
n1 = float (input("Digite o primeiro número: "))
n2 = float (input("Digite o segundo número: "))
op = input("Digite a operação desejada (+, -, *, /): ")
if op == "+":
 print("resultado",  n1 + n2)
elif op == "-":
    print("resultado", n1 - n2)
elif op == "*":
    print("resultado", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("resultado", n1 / n2)
    else:
      print("Operação inválida.")
"""
