import json
import random
from datetime import datetime
from pathlib import Path
from cli.cli import * 
from dificuldades.dificuldades import *
from persistência_De_Dados.persistencia_de_dados import * 
from regras_e_tabuleiro.regras_e_tabuleiro import *

def jogar_partida(dificuldade):
    tabuleiro = criar_tabuleiro()
    simbolo_humano = "X"
    simbolo_pc = "O"
    turno = "humano"

    print(f"\nInício da partida - dificuldade {dificuldade}.")
    print("Tu jogas com X; o computador joga com O.")
    mostrar_tabuleiro(tabuleiro)

    while True:
        if turno == "humano":
            posicao = pedir_jogada_humano()
            if not aplicar_jogada(tabuleiro, posicao, simbolo_humano):
                print("Essa casa já está ocupada. Escolhe outra.")
                continue
            turno = "computador"
        else:
            posicao = escolher_jogada(tabuleiro, dificuldade, simbolo_pc, simbolo_humano)
            if posicao is not None:
                aplicar_jogada(tabuleiro, posicao, simbolo_pc)
                print("O computador jogou na casa", posicao + 1)
            turno = "humano"

        mostrar_tabuleiro(tabuleiro)
        resultado = verificar_vencedor(tabuleiro)
        if resultado is not None:
            if resultado == simbolo_humano:
                print("Parabéns! Ganhaste!")
                guardar_partida("humano", dificuldade)
            elif resultado == simbolo_pc:
                print("O computador ganhou!")
                guardar_partida("computador", dificuldade)
            else:
                print("Empate!")
                guardar_partida("empate", dificuldade)
            break


def main():
    while True:
        opcao = menu_principal()
        if opcao == "1":
            dados = carregar_dados()
            anterior = dados["preferencias"].get("dificuldade", "facil")
            if anterior not in ("facil", "medio"):
                anterior = "facil"
            dificuldade = escolher_dificuldade(anterior)
            guardar_preferencia(dificuldade)
            jogar_partida(dificuldade)
        elif opcao == "2":
            mostrar_estatisticas()
        elif opcao == "3":
            print("Até à próxima no TicTacPy!")
            break
        else:
            print("Opção inválida. Escolhe 1, 2 ou 3.")


if __name__ == "__main__":
    main()
