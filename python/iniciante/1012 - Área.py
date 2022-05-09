a, b, c = [float(x) for x in input().split()]
pi = 3.14159

triang = (a*c)/2
circ = (pi*(c*c))
trap = ((a+b)*c)/2
quad = b**2
ret = a*b

print("TRIANGULO: %0.3f"%triang)
print("CIRCULO: %0.3f"%circ)
print("TRAPEZIO: %0.3f"%trap)
print("QUADRADO: %0.3f"%quad)
print("RETANGULO: %0.3f"%ret)
