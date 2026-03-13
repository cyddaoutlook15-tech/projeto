def mostrar_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print("\n")
    
def verificar_vitoria(tabuleiro, jogador):
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    
    for vitoria in vitorias:
        if all(tabuleiro[i] == jogador for i in vitoria):
            return True
    return False
    
