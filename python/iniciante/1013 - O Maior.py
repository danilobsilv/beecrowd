maior = 0
a,b,c = [int(x) for x in input().split()]

maiorAB = ((a+b) + abs(a-b))/2
if maiorAB > c:
    maior = maiorAB
    print("%0.0f eh o maior"%maior)
else:
    maior = c
    print("%0.0f eh o maior"%maior)
