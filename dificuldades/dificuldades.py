import random
from regras_e_tabuleiro.regras_e_tabuleiro import *

def jogada_aleatoria(tabuleiro):
    livres = obter_posicoes_livres(tabuleiro)
    if livres:
        return random.choice(livres)
    return None


def procurar_jogada_vencedora(tabuleiro, simbolo):
    """Devolve uma casa onde o símbolo faz três em linha, se existir."""
    for posicao in obter_posicoes_livres(tabuleiro):
        tabuleiro[posicao] = simbolo  # Experimenta a jogada
        venceu = verificar_vencedor(tabuleiro) == simbolo
        tabuleiro[posicao] = " "      # Desfaz a experiência
        if venceu:
            return posicao
    return None


def jogada_estrategica(tabuleiro, simbolo_pc="O", simbolo_humano="X"):
    
    livres = obter_posicoes_livres(tabuleiro)
    if not livres:
        return None

    
    posicao = procurar_jogada_vencedora(tabuleiro, simbolo_pc)
    if posicao is not None:
        return posicao

    
    posicao = procurar_jogada_vencedora(tabuleiro, simbolo_humano)
    if posicao is not None:
        return posicao

    
    if 4 in livres:
        return 4

    
    cantos_opostos = [(0, 8), (2, 6), (6, 2), (8, 0)]
    for canto_jogador, canto_oposto in cantos_opostos:
        if tabuleiro[canto_jogador] == simbolo_humano and canto_oposto in livres:
            return canto_oposto

    
    cantos_livres = []
    for posicao in (0, 2, 6, 8):
        if posicao in livres:
            cantos_livres.append(posicao)
    if cantos_livres:
        return random.choice(cantos_livres)

    
    return random.choice(livres)


def escolher_jogada(tabuleiro, dificuldade, simbolo_pc="O", simbolo_humano="X"):
    if dificuldade == "facil":
        return jogada_aleatoria(tabuleiro)
    return jogada_estrategica(tabuleiro, simbolo_pc, simbolo_humano)
