N = int(input())
lista = []
for x in range(N):
    entrada = int(input())
    lista.append(entrada)
dentro = 0
fora = 0 
for elem in lista:
    if 10 <= elem <= 20:
        dentro += 1
    elif elem < 10 or elem > 20:
        fora += 1
print(f"{dentro} in")
print(f"{fora} out")
