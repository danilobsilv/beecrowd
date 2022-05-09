citiesDict = {61:"Brasilia", 71:"Salvador", 11:"Sao Paulo", 21:"Rio de Janeiro", 32:"Juiz de Fora", 19:"Campinas", 27:"Vitoria", 31: "Belo Horizonte"}
ddd = int(input())
if ddd in citiesDict:
    print(citiesDict[ddd])
elif ddd not in citiesDict:
    print("DDD nao cadastrado")
