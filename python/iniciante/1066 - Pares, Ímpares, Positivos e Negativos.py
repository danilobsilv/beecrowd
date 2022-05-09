lista  = []

for x in range(5):
    entrada = int(input())
    lista.append(entrada)

pares = 0
impares = 0

positivos = 0
negativos = 0

for elem in lista:
    if elem%2 == 0:
        pares += 1
    elif elem%2 != 0:
        impares += 1

for elem in lista:
    if elem > 0:
        positivos += 1
    elif elem < 0:
        negativos += 1
    elif elem == 0:
        positivos += 0

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
