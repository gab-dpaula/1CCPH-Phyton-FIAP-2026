nomes = ["Ale", "João", "Max", "Bob"]

#duplas = []

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        #duplas.append([nomes[i],nomes[j]])
        print(f"{nomes[i]} - {nomes[j]}")

        # Expecíficar as duas linhas que desejo colocar na lista