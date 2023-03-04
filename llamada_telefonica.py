# programa para saber el costo de una llamada

print("-----------------------------")
print("----costo de la llamada------")
print("-----------------------------")

# input

dl= int(input("ingrese el tiempo de la llamada"))

# processing

if (dl<= 3):
    print(" el valor de la llamada es 300 pesos")

else:
    t= dl-3
    cl= 300+50*t
    print("el valor de la llamada es "+ str(cl) )