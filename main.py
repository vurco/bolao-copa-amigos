import csv

# --- CONFIGURAÇÃO DO RESULTADO REAL ---
# (Mude aqui quando o jogo acabar!)
RESULTADO_REAL = {"time1": 2, "time2": 0} 

def calcular_ranking():
    ranking = {} # Dicionário para guardar {Nome: Pontos}

    try:
        with open('palpites.csv', mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                nome = linha['Nome']
                g1 = int(linha['Gols1'])
                g2 = int(linha['Gols2'])
                
                pontos = 0
                # Regra: Placar Exato = 10 pontos
                if g1 == RESULTADO_REAL["time1"] and g2 == RESULTADO_REAL["time2"]:
                    pontos = 10
                # Regra: Acertou o vencedor ou empate = 5 pontos
                elif (g1 > g2 and RESULTADO_REAL["time1"] > RESULTADO_REAL["time2"]) or \
                     (g1 < g2 and RESULTADO_REAL["time1"] < RESULTADO_REAL["time2"]) or \
                     (g1 == g2 and RESULTADO_REAL["time1"] == RESULTADO_REAL["time2"]):
                    pontos = 5
                
                # Soma os pontos ao total do jogador
                ranking[nome] = ranking.get(nome, 0) + pontos
        
        # Ordenar o ranking do maior para o menor
        ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
        return ranking_ordenado

    except FileNotFoundError:
        return []

# --- EXIBIÇÃO ---
print("\n--- 🏆 RANKING ATUALIZADO ---")
lista_ranking = calcular_ranking()

if not lista_ranking:
    print("Nenhum palpite registrado ainda.")
else:
    for i, (nome, pts) in enumerate(lista_ranking, 1):
        print(f"{i}º - {nome}: {pts} pontos")

