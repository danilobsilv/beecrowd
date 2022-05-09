lista = []
for x in range(100):
    entrada = int(input())
    lista.append(entrada)

x = max(lista,key=int)
print(x)

for index, num in enumerate(lista):
    if num == x:
        print(f"{index+1}")
