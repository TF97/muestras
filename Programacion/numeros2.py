num1 = int(input("escriba el primer numero: "))
num2 = int(input("escriba el segundo numero: "))
promedio = (num1 + num2) / 2

if promedio >= 7:
    print("esta aprobado")
elif promedio <= 5:
    print("esta desaprobado")
else:
    print("debe recursar")        
    
print(promedio)    