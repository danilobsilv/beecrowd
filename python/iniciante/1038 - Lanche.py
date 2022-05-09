menu_dict = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

cod, qtde = [float(x) for x in input().split()]

print(f"Total: R$ {(menu_dict[cod])*qtde:.2f}")
