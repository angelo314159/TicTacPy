LINHAS_VITORIA = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def criar_tabuleiro():
    return [" "] * 9


def validar_jogada(tabuleiro, posicao):
    return 0 <= posicao < 9 and tabuleiro[posicao] == " "


def aplicar_jogada(tabuleiro, posicao, simbolo):
    if validar_jogada(tabuleiro, posicao):
        tabuleiro[posicao] = simbolo
        return True
    return False


def obter_posicoes_livres(tabuleiro):
    livres = []
    for posicao in range(9):
        if tabuleiro[posicao] == " ":
            livres.append(posicao)
    return livres


def verificar_vencedor(tabuleiro):
    for a, b, c in LINHAS_VITORIA:
        if tabuleiro[a] != " " and tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return tabuleiro[a]
    if " " not in tabuleiro:
        return "empate"
    return None
