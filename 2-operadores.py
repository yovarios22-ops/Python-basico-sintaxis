#operadores en python 
#yovani
#1. operadores aritmeticos 
suma = 5 + 5
resta = 10-6
multiplicacion = 5 * 5
division = 10 / 2
modulo = 10 % 2 
exponente = 10 ** 2


print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(exponente)

#2. operadores de comparacion 
print(5 ==5 )    # igual a 
print(5 != 5)    #diferente de 
print(10 > 5 )   #mayor que
print(10 < 5 )   #menor que 
print(10 >= 5 )  #mayor igual que
print(10 <= 5 )  #menor igual que

#3. operadores logicos 
v = True
f = False
#3.1 and (y)
print('-------------------------AND')
print(v and v)
print(v and f)
print(f and v)
print(f and f)
#3.2 or (o)
print(v or v)
print(v or  f)
print(f or v)
print(f or f)
#3.3 not (negacion)
print('-------------------------NOT')
print(not f)
print(not v)

#4. operadores de asignación
# suma y asigna (+=)
print("------------------------------+=")
edad = 20
edad +=5 
print(edad)

print("-------------------------------=")
#resta y asigna (-=)
saldo = 100
saldo -=10
print(saldo)

print("------------------------------*=")
#multiplica y asigna(*=)
precio = 30
precio *= 5
print(precio)

print("------------------------------/=")
#divide y asigna (/=)
total = 200
total /= 2
print(total)
 