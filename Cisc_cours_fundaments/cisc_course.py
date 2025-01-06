var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name, sep='-', end=' _Siguiente linea_ ')
print(var)

john, mary, adam = 3, 5, 6
print(john, mary, adam, sep=',')
total_apples = john + mary + adam
print(total_apples)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

# Round redondea a los numeros de decimales especificados
# Retorna un valor flotante
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

z = y = x = 1
print(x, y, z, sep='*')

x = int(input("Ingrese un valor para x: "))
y = int(input("Ingrese un valor para y: "))

x = x // y
y = y // x

print(y)
