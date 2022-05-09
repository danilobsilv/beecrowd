while True:
    x,y = [int(x) for x in input().split()]
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
    elif x == y:
        break
