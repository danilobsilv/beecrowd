for x in range(int(input())):
    try:
        n1, n2 = [int(x) for x in input().split()]
        resultado = n1/n2
    except ZeroDivisionError:
        print("divisao impossivel")
    else:
        print(resultado)
