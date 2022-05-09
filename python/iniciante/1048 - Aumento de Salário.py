s = float(input())
if 0 <= s <= 400:
    novo_salario = (s*0.15) + s
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {s*0.15:.2f}")
    print("Em percentual: 15 %")

elif 400.01 <= s <= 800:
    novo_salario = (s*0.12) + s
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {s*0.12:.2f}")
    print("Em percentual: 12 %")

elif 800.01 <= s <= 1200:
    novo_salario = (s*0.1) + s
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {s*0.1:.2f}")
    print("Em percentual: 10 %")

elif 1200.01 <= s <= 2000:
    novo_salario = (s*0.07) + s
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {s*0.07:.2f}")
    print("Em percentual: 7 %")

elif s > 2000:
    novo_salario = (s*0.04) + s
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {s*0.04:.2f}")
    print("Em percentual: 4 %")
