#yovani.Z
#tuplas sets y diccionarios

#tuplas
#simbolo ()
#por default lo ordena
#inmutables = no se puede hacer cambios
#te acepta duplicados

tupla = (1, 2, 1, 2, 40, 10,5, 11)
print(tupla)

#indices
print(tupla[4])

print("-------------------")
#sets
# simbolo {} 
# no ordena 
# mutable = si se puede hacer cambios 
#no acepta duplicados
sets = {1,2,3,1,2,3}
print(sets)
#add () agregar un nuevo dato
sets.add(4)
print(sets)
#remove() eliminar un dato
sets.remove(3)
print(sets)

print("----------")
# diccionarios 
#simbolo {key:value}
# si ordena

estudiante = {
    "nombre" : "Yovani",
    "natalidad" : "Chucuito",
    "edad" : 18,
    "carrera":"ingenieria"
}
print (estudiante)

print(estudiante["nombre"])
print(estudiante["natalidad"])
print(estudiante["edad"])
print(estudiante["carrera"])

estudiante["edad"] = 40
print(estudiante)

#ciclo for en los diccionarios 
for clave, valor in estudiante.items():
    print("Clave: ", clave , "Valor: ", valor)
