import json
import random
from datetime import datetime

FICHEIRO_DADOS = Path(__file__).resolve().parent / "tictacpy_dados.json"


def dados_iniciais():
    return {"historico": [], "preferencias": {"dificuldade": "facil"}}


def carregar_dados():
    if not FICHEIRO_DADOS.exists():
        return dados_iniciais()
    try:
        with FICHEIRO_DADOS.open("r", encoding="utf-8") as ficheiro:
            dados = json.load(ficheiro)
        if isinstance(dados, dict) and isinstance(dados.get("historico"), list):
            if not isinstance(dados.get("preferencias"), dict):
                dados["preferencias"] = {}
            return dados
    except (OSError, json.JSONDecodeError):
        print("Aviso: não foi possível ler os dados. Será usado um histórico novo.")
    return dados_iniciais()


def guardar_dados(dados):
    try:
        with FICHEIRO_DADOS.open("w", encoding="utf-8") as ficheiro:
            json.dump(dados, ficheiro, indent=4, ensure_ascii=False)
        return True
    except OSError:
        print("Não foi possível guardar os dados no ficheiro JSON.")
        return False


def guardar_preferencia(dificuldade):
    dados = carregar_dados()
    dados["preferencias"]["dificuldade"] = dificuldade
    guardar_dados(dados)


def guardar_partida(vencedor, dificuldade):
    dados = carregar_dados()
    dados["historico"].append({
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "vencedor": vencedor,
        "dificuldade": dificuldade,
    })
    guardar_dados(dados)


def obter_estatisticas():
    partidas = carregar_dados()["historico"]
    return {
        "total": len(partidas),
        "vitorias": sum(1 for p in partidas if p.get("vencedor") == "humano"),
        "derrotas": sum(1 for p in partidas if p.get("vencedor") == "computador"),
        "empates": sum(1 for p in partidas if p.get("vencedor") == "empate"),
    }


def mostrar_estatisticas():
    est = obter_estatisticas()
    print("\n--- Estatísticas ---")
    print("Total de partidas:", est["total"])
    print("Vitórias:", est["vitorias"])
    print("Derrotas:", est["derrotas"])
    print("Empates:", est["empates"])
    input("\nPrime Enter para voltar ao menu...")

