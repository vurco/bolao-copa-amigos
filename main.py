import csv
import os

ARQUIVO = 'palpites_copa.csv'

# Simulando os resultados reais de vários jogos
RESULTADOS_OFICIAIS = {
    "Brasil x Sérvia": (2, 0),
    "Portugal x Gana": (3, 2),
    "França x Austrália": (4, 1)
}

def inicializar_bd():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Nome', 'Jogo', 'Gols1', 'Gols2'])

def salvar_palpite(nome, jogo, g1, g2):
    with open(ARQUIVO, mode='a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([nome, jogo, g1, g2])

def calcular_ranking():
    ranking = {}
    with open(ARQUIVO, mode='r', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            nome = linha['Nome']
            jogo = linha['Jogo']
            g1, g2 = int(linha['Gols1']), int(linha['Gols2'])
            
            # Busca o resultado real para ESSE jogo
            if jogo in RESULTADOS_OFICIAIS:
                res_g1, res_g2 = RESULTADOS_OFICIAIS[jogo]
                
                pts = 0
                if g1 == res_g1 and g2 == res_g2:
                    pts = 10
                elif (g1 > g2 and res_g1 > res_g2) or (g1 < g2 and res_g1 < res_g2) or (g1 == g2 and res_g1 == res_g2):
                    pts = 5
                
                ranking[nome] = ranking.get(nome, 0) + pts
    return ranking

# --- TESTE ---
inicializar_bd()
print("Jogos disponíveis:", list(RESULTADOS_OFICIAIS.keys()))
j = input("Qual jogo deseja apostar? ")
n = input("Seu nome: ")
p1 = int(input("Gols Time 1: "))
p2 = int(input("Gols Time 2: "))

salvar_palpite(n, j, p1, p2)

print("\n--- 🏆 RANKING GERAL ---")
ranking_final = calcular_ranking()
for nome, pontos in sorted(ranking_final.items(), key=lambda x: x[1], reverse=True):
    print(f"{nome}: {pontos} pts")


