def mostrar_cabecalho():
    print("\n" + "=" * 35)
    print("       TicTacPy - Sprint 2")
    print("          Jogo do Galo")
    print("=" * 35)


def mostrar_tabuleiro(tabuleiro):
    casas = []
    for posicao in range(9):
        if tabuleiro[posicao] == " ":
            casas.append(str(posicao + 1))
        else:
            casas.append(tabuleiro[posicao])

    print()
    print(f" {casas[0]} | {casas[1]} | {casas[2]}")
    print("---+---+---")
    print(f" {casas[3]} | {casas[4]} | {casas[5]}")
    print("---+---+---")
    print(f" {casas[6]} | {casas[7]} | {casas[8]}")
    print()


def menu_principal():
    mostrar_cabecalho()
    print("1. Jogar contra o computador")
    print("2. Ver estatísticas")
    print("3. Sair")
    return input("Escolhe uma opção: ").strip()


def escolher_dificuldade(dificuldade_anterior):
    print("\nEscolhe a dificuldade:")
    print("1. Fácil - computador joga ao acaso")
    print("2. Médio - computador usa uma estratégia")
    print(f"Enter = manter a anterior ({dificuldade_anterior})")
    while True:
        opcao = input("Opção (1/2): ").strip()
        if opcao == "1":
            return "facil"
        if opcao == "2":
            return "medio"
        if opcao == "":
            return dificuldade_anterior
        print("Opção inválida. Escolhe 1 ou 2.")


def pedir_jogada_humano():
    while True:
        resposta = input("Em que casa queres jogar? (1-9): ").strip()
        if resposta.isdigit() and 1 <= int(resposta) <= 9:
            return int(resposta) - 1  
        print("Jogada inválida. Introduz um número de 1 a 9.")
