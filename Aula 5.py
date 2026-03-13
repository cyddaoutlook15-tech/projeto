"""
numeros = [1, 2, 3, 4, 5]

for i in range(5):
    valor = float(input("Digite um número: "))
    numeros[i] = valor
    print("Listas completas:", numeros)
    print("Maior valor:" , max(numeros))
    print("Menor valor:", min(numeros))
    """
    
    
"""   
numeros = []

while True:
    valor = float(input("Digite um numero:"))
    numeros.append(valor)
    
    continuar = input("Deseja continuar? (s/n): ").strip().upper()
    if continuar == "N":
        break
    
    pares = []
    impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero) 
print("Lista original:", numeros)
print("Lista de pares:", pares)
print("Lista de ímpares:", impares)
"""

"""
def area(largura, comprimento):
    resultado = largura * comprimento
    print(f"A área é {resultado}m²")
area(5, 100)
"""


"""
def fatorial(n):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
    return resultado
numero = int(input("Digite um número para calcular o fatorial: "))  
resultado_fatorial = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado_fatorial}")  
"""  


"""
from datetime import date

def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    
    if idade < 16:
        return "Não vota"
    elif 16 <= idade < 18 or idade >= 70:
        return "Voto opcional"
    else:
        return "Voto obrigatório"

ano= int(input("Digite seu ano de nascimento: "))
resultado_voto = voto(ano)  
print(f"Situação do voto: {resultado_voto}")
"""


"""
matriz = []
soma_pares = 0

for linha in range(3):
    linha_matriz = []
    for coluna in range(3):
        valor = int(input(f"Digite o valor para a posição [{linha}][{coluna}]: "))
        linha_matriz.append(valor)
        if valor % 2 == 0:
            soma_pares += valor
    matriz.append(linha_matriz)

print("\n Soma dos valores pares:", soma_pares)
"""


"""
def notas(*n):
    resultado =["quantidade de notas:", len(n), "média das notas:", sum(n)/len(n)]
    resultado =["maior nota:", max(n), "menor nota:", min(n)]
    media = sum(n)/len(n)
    
    if media >= 7:
        resultado["Situação"]= "Aprovado"
    else:
        resultado["Situação"]= "Reprovado"
    return resultado

notas(5, 7, 8, 6, 9)   
print("Resultado:", notas(5, 7, 8, 6, 9))
"""
