#ejercicio02
#declaracion de variables
cliente,producto,cantidad,costo_de_unidad="","",0,0.0
cliente=str(input("ingrese nombre del cliente:"))
producto=str(input(input("ingrese nomnre del  producto: ")))
cantidad=int(input("ingrese cantidad: "))
costo_de_unidad=float(input("ingrese el costo de unidad:"))
#processing
T=cantidad*costo_de_unidad
comprador_impulsivo=T>250
if (comprador_impulsivo):
    print("comprador impulsivo")
else:
    print("si es comprador impulsivo")
