texto = "FIAP Paulista"

print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])

tamanho = len(texto)
print(tamanho)
print()

for i in range(tamanho):
    print(f"texto[{i}] = {texto[i]}")

# em C
#int tamanho = 13
#for(int i=0; i< tamanho; i++)

for letra in texto:
    print(letra)