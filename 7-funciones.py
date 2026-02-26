#yovani.Z
#funciones 

print("Hola, Juan")
print("Bienvenido al sistema")
print("----------------------")

print("Hola, Yovani")
print("Bienvenido al sistema")
print("----------------------")

print("Hola, Pepito")
print("Bienvenido al sistema")
print("----------------------")

print("------------")

nombres=["Yovani" , "diego" , "pepito"]
for i in nombres:
    print("hola", i)
    print("bienvenido al sistema")
    print("----------------")

print("=====================")

def saludar(nombre):
    print("hola",nombre)
    print("bienvenido al sistema")
    print("-------------")
saludar("Juan")
saludar("Diego")
saludar("Pepito")

print("-----------------------------------------xd")
# funciones con retorno return()
def suma(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    return(resultado)

    #return(primer_numero + segundo_numero)
    
print(suma(2,2))

#funciones sin retorno

def suma2(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    print(resultado)

suma2(2,2)


