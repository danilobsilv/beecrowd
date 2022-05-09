counter = 0
for x in range(5):
    entrada = int(input())
    if (entrada%2) == 0: 
        counter += 1
print(f"{counter} valores pares")
