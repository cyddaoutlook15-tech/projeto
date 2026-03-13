#Exercício 1
"""     
nome = input("Digite seu nome: ")
media = float(input("Digite sua média: "))

aluno = {"nome": nome, "media": media}

if aluno["media"] >= 7:
    print("Parabéns, você foi aprovado!")
elif aluno["media"] >= 5:
    print("Você está de recuperação.")
else:
    print("Infelizmente, você foi reprovado.")
"""
#Exercício 2

"""
import random
jogadores = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4"]
sorteado = random.choice(jogadores)
print(f"O jogador sorteado é: {sorteado}")

ranking = {"Jogador 1": 0, "Jogador 2": 0, "Jogador 3": 0, "Jogador 4": 0}
ranking[sorteado] += 1

print("Ranking dos jogadores:")
for jogador, pontos in ranking.items():
    print(f"{jogador}: {pontos} pontos")  
"""

#Exercício 3


"""
from datetime import datetime
ano_atual = datetime.now().year

dados = {}
dados["nome"] = input("Nome:") 
dados["ano_nascimento"] = int(input("Ano de nascimento:")) 
dados["idade"] = ano_atual- dados["ano_nascimento"]
dados["ctps"] = int(input("Número da carteira de trabalho (0 se não tiver):"))

if dados["ctps"] != 0:
    dados["ano_contratacao"] = int(input("Ano de contratação:"))
    dados["salario"] = float(input("Salário:"))
    dados["aposentadoria"] = dados["idade"] + (dados["ano_contratacao"] + 35 - ano_atual)
else:
    dados["ano_contratacao"] = 0
    dados["salario"] = 0
    dados["aposentadoria"] = "N/A"
print("Dados do trabalhador:")
for chave, valor in dados.items():
    print(f"{chave}: {valor}")
    """


#Exercício 4

"""
jogadores ={}
gols = []

jogadores["nome"] = input("Nome do jogador: ")
partidas = int(input("Número de partidas jogadas: "))

for i in range(partidas):
    gols.append(int(input(f"Gols na partida {i+1}: ")))
jogadores["gols"] = gols
jogadores["total_gols"] = sum(gols)
print("Dados do jogador:")
for chave, valor in jogadores.items():
    print(f"{chave}: {valor}")
"""

#Exercício 5

"""
pessoas = []
soma_idades = 0

while True:
    dados = {}
    dados["nome"] = input("Nome: ")
    dados["idade"] = int(input("Idade: "))
    dados["sexo"] = input("Sexo (M/F): ")
    
    pessoas.append(dados.copy())
    soma_idades += dados["idade"]
    
    resp = input("Deseja continuar? (S/N): ")
    if resp.upper() == "N":
        break

print(f"\nA )Total de pessoas cadastradas: {len(pessoas)}")


media = soma_idades / len(pessoas) if pessoas else 0
print(f"B)Média de idade: {media:.2f}")

print("C)Lista de mulheres cadastradas:")
for p in pessoas:
    if p["sexo"] in "Ff":
        print(p["nome"])
        
        print("D)Lista de pessoas com idade acima da média:")
for p in pessoas:
    if p["idade"] > media:
        print(f"{p['nome']} - {p['idade']} anos")

"""

#Exercício 6

"""
time = []

while True:
    jogador = {}
    jogador["nome"] = input("Nome do jogador: ")
    jogador["gols"] = int(input("Número de gols: "))
    
    time.append(jogador.copy())
    
    resp = input("Deseja continuar? (S/N): ")
    if resp.upper() == "N":
        break
    
    while True:
        cod = int(input("Digite o código do jogador(999 para sair): "))
        if cod == 999:
            break
        elif 0 <= cod < len(time):
            jogador_atualizado = time[cod]
            print(f"Jogador selecionado: {jogador_atualizado['nome']} - Gols: {jogador_atualizado['gols']}")
            jogador_atualizado["gols"] = int(input(f"Digite o novo número de gols para {jogador_atualizado['nome']}: "))
            print("Gols atualizados com sucesso!")
        else:
            print("Código inválido. Tente novamente.")
    
    
    
print("\nDados dos jogadores:")
for i, jogador in enumerate(time):
    print(f"Jogador {i+1}: {jogador['nome']} - Gols: {jogador['gols']}")
    jogador["gols"] = int(input(f"Atualize os gols de {jogador['nome']}: "))    
print("\nDados atualizados dos jogadores:")
for i, jogador in enumerate(time):
    print(f"Jogador {i+1}: {jogador['nome']} - Gols: {jogador['gols']}")    
"""
    
    


