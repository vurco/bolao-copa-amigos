import csv

# Função para salvar o palpite no arquivo CSV
def salvar_palpite(nome, t1, g1, g2, t2):
    # 'a' significa 'append' (anexar), para não apagar o que já existe
    with open('palpites.csv', mode='a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, t1, g1, g2, t2])
    print(f"✅ Sucesso! O palpite de {nome} foi guardado na memória.")

# --- INTERFACE SIMPLIFICADA ---
print("--- Cadastro de Palpites ---")
usuario = input("Nome do apostador: ")
time_a = "Brasil"
time_b = "Sérvia"
gols_a = input(f"Gols do {time_a}: ")
gols_b = input(f"Gols do {time_b}: ")

# Chamando a função para salvar
salvar_palpite(usuario, time_a, gols_a, gols_b, time_b)
