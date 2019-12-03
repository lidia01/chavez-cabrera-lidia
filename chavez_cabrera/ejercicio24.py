#ejercicio24
#declaracion de variables
precio_sin_igv,total=0.0,0.0
precio_sin_igv=float(input("ingrese el precio sin iva:"))
total=float(input("ingrese total:"))

#PROCESING
total_igv=(total-precio_sin_igv)
if (total>1.2):
    print("igv incluido")
#fin_if
