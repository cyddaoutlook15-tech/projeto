# Jogo da Velha - Main.py

from Jogo import jogar

while True:
    print("Bem-vindo ao Jogo da Velha #!")
    print("Escolha o modo de jogo:")
    print("1 - Jogar")
    print("2 - Sair")
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == '1':
        jogo = jogar()
    
    elif escolha == '2':
        print("Saindo do JOGO!")
        
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
    
