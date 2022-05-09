n = int(input())
qtdeC = []
qtdeR = []
qtdeS = []
for x in range(n):
    quantidade, tipo = input().split()
    
    quantidade = int(quantidade)
    tipo = str(tipo)

    if tipo == "C":
        qtdeC.append(quantidade)
    elif tipo == "R":
        qtdeR.append(quantidade)
    elif tipo == "S":
        qtdeS.append(quantidade)

SomaTotal = sum(qtdeC) + sum(qtdeR) + sum(qtdeS)

print(f"Total: {SomaTotal} cobaias")
print(f"Total de coelhos: {sum(qtdeC)}")
print(f"Total de ratos: {sum(qtdeR)}")
print(f"Total de sapos: {sum(qtdeS)}")
print(f"Percentual de coelhos: {(sum(qtdeC)/SomaTotal)*100:.2f} %")
print(f"Percentual de ratos: {(sum(qtdeR)/SomaTotal)*100:.2f} %")
print(f"Percentual de sapos: {(sum(qtdeS)/SomaTotal)*100:.2f} %")
