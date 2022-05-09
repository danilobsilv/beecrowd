contador = 0
notas = []
while True:
    nota = float(input())

    if nota < 0:
        print("nota invalida")
        continue
    elif nota > 10:
        print("nota invalida")
        continue
    
    if 0 <= nota <= 10:
        notas.append(nota)
        contador += 1

    if contador == 2:
        
        print(f"media = {sum(notas)/2}")
        break
