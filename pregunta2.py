lista=[]
i=0

while len(lista)<5:
    i=i+1
    x=int(input("Ingresar numero"+str(i)+":  "))

    lista.append(x)
print(lista)

minimo=lista[0]
def  menor_en_arreglo(lista):
    for i in lista:
        if i < minimo:
            minimo=i

print (minimo)
    