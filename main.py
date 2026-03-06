# --- SISTEMA DE PONTOS DO BOLÃO ---

print("=== Bem-vindo ao Sistema do Bolão ===")

# Simulando entrada de dados
nome_jogador = input("Digite o nome do amigo: ")
palpite_time1 = int(input(f"Gols do Time A ({nome_jogador}): "))
palpite_time2 = int(input(f"Gols do Time B ({nome_jogador}): "))

# Resultado Real (Isso você mudará quando o jogo acabar)
resultado_time1 = 2
resultado_time2 = 1

# Lógica de Pontuação
pontos = 0

if palpite_time1 == resultado_time1 and palpite_time2 == resultado_time2:
    pontos = 10
    print(f"🔥 Placar exato! {nome_jogador} ganhou {pontos} pontos.")
elif (palpite_time1 > palpite_time2 and resultado_time1 > resultado_time2) or \
     (palpite_time1 < palpite_time2 and resultado_time1 < resultado_time2) or \
     (palpite_time1 == palpite_time2 and resultado_time1 == resultado_time2):
    pontos = 5
    print(f"✅ Acertou o vencedor/empate! {nome_jogador} ganhou {pontos} pontos.")
else:
    print(f"❌ Errou feio! {nome_jogador} ganhou {pontos} pontos.")
