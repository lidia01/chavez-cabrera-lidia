#ejercicio10
#declaracion de variables
enero,febrero,marzo,abril,mayo,junio,igv=0.0,0.0,0.0,0.0,0.0,0.0,0.0
enero=float(input("ingrese enero:"))
febrero=float(input("ingrese febrero:"))
marzo=float(input("ingrese marzo:"))
abril=float(input("ingrese abril:"))
mayo=float(input("ingrese mayo:"))
junio=float(input("ingrese junio:"))
igv=float(input("ingreso igv:"))
#processing
promedio=(enero+febrero+marzo+abril+mayo+junio)/7+igv
if(promedio < 69):
    print("promedio gastado")
else:
    print("promedio gastado")
