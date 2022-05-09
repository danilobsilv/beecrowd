while True:
    x,y = [int(x) for x in input().split()]

    if x == 0 or y == 0:
        break
    if x > 0 and y > 0:
        print("primeiro")
    if x > 0 and y < 0:
        print("quarto")
    if x < 0 and y > 0:
        print("segundo")
    if x < 0 and y< 0:
        print("terceiro")
