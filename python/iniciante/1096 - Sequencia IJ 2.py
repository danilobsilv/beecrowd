I = 1
J = 7

while True:
    print(f"I={I} J={J}")
    print(f"I={I} J={J-1}")
    print(f"I={I} J={J-2}")
    I += 2
    if I > 9:
        break
