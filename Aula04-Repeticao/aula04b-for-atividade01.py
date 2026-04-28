# atividade 3

qtd_musicas = int(input("Qtd de mscs (DB): "))

for i in range(qtd_musicas):
    print(f"Música {i}")


#   Repetição encadeada ou laços alinhados
for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f"i: {i}, j:{j}")
