counter = 0
n = int(input())
for x in range(1,n+1):
    if (x%2) == 0:
        counter += 2
        print(f"{counter}^2 = {x**2}")
