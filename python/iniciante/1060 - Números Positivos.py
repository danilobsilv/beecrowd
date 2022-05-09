lista = []

for x in range(6):
    entrada = float(input())
    lista.append(entrada)
contador = 0
for elem in lista:
    if elem > 0:
        contador = contador + 1

print(f"{contador} valores positivos")
