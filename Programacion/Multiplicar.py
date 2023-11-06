def tabla_del(numero):
    resultado = []
    for i in range(11):
        resultado.append(numero * i)
    return resultado
    
# programa pricipal
res = tabla_del(3)
print(res)    