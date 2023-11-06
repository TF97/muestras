from datetime import datetime

dt = datetime.now()

print(dt)
print("Año:", dt.year)
print("Mes:", dt.month)
print("Dia:", dt.day)

print("Hora:", dt.hour)
print("Minuto:", dt.minute)
print("Segundo:", dt.second)
print("Microsegundo:", dt.microsecond)

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}".format(dt.day, dt.month, dt.year))