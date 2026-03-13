from utilidades import mostrar_tabuleiro, verificar_vitoria

def jogar():
    tabuleiro =[""] * 9
    jogador_atual = "X"
    
    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogador_atual}.")
        
        try:
            posicao = int(input("Digite a posição (1-9) onde deseja jogar: ")) - 1
            if posicao < 0 or posicao > 8:
                print("Posição inválida. Tente novamente.")
                continue
            if tabuleiro[posicao] != "":
                print("Essa posição já está ocupada. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, digite um número de 1 a 9.")
            continue
        
        tabuleiro[posicao] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador_atual} venceu!")
            break
        
        if "" not in tabuleiro:
            mostrar_tabuleiro(tabuleiro)
            print("Empate! O jogo terminou sem vencedores.")
            break
        
        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"
