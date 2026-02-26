#yovani
#listas
lista = ["Yovani", "Mamani", 25,True]
print(lista[0])

#lista de frutas
frutas = ['manzana','uva','fresa','platano','mango']
print (frutas[3])

frutas[1] = "granada"
print(frutas)
for i in frutas:
    print(i)

print('-----------------------------------')
#matriz
matriz = [
    [1,2,3],
    [4,6,1],
    [0,1,0]
]
print (matriz [2][2])

#lista de numeros 
numeros = [1,2,3,4,5,6,7,8,9,0]
print(numeros[8])
print(numeros[:3])
print(numeros[1:5])
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])

#ciclo for en las listas 
for i in numeros:
    print(i*10)

#metodos en las listas
print("_------------------------------------ METODOS")
frutas = ['manzana','uva','fresa','platano','mango']
#agregar un nuevo dato a la lista = insertar un dato
frutas.append("ciruela")
print(frutas)

#insert 
frutas.insert(2,"pera")
print(frutas)

#remove = borrar
frutas.remove("uva")
print(frutas)

#pop = para obtener o eliminar el ultimo dato 
frutas.pop()
print(frutas)

#sort() = ordenar la lista
frutas.sort()
print(frutas)

#reverse() = revertir 
frutas.reverse()
print(frutas)
print("--")
#len() = contar datos
cantidad = len(frutas)
print(cantidad)
print("--")
#index() = encontrar el indice 
indice = frutas.index("mango")
print(indice)
