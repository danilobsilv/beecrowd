peca1, qtd1, vUnit1 = map(float, input().split())
peca2, qtd2, vUnit2 = map(float, input().split())

val = (qtd1*vUnit1) + (qtd2*vUnit2)

print("VALOR A PAGAR: R$ %0.2f"%val)
