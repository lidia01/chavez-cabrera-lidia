#ejercicio07
#declaracion de variables
nombre,pasaje1,pasaje2,pasaje3,pasaje4,igv="",0.0,0.0,0.0,0.0,0.0
nombre=input("ingrese nombre:")
pasaje1=float(input("ingrese pasaje1:"))
pasaje2=float(input("ingrese pasaje2:"))
pasaje3=float(input("ingrese pasaje3:"))
pasaje4=float(input("ingrese pasaje4:"))
igv=float(input("ingrese igv:"))
#processing
total=(pasaje1+pasaje2+pasaje3+pasaje4)
if (nombre=="lidia") and (total > 120):
    print("comprador impulsivo")
else:
    print("no es comprador impulsivo")
