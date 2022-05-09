D = int(input())
Y = 0
M = 0

while (D >= 365):
    D -= 365
    Y += 1

while (D >= 30) and (D < 365):
    D -= 30
    M += 1

print(f"{Y} ano(s)")
print(f"{M} mes(es)")
print(f"{D} dia(s)")
