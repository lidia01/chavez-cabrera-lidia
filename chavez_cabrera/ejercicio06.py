#ejercicio06
#declaracion de variables
nombre_del_comprador,puerta_acrilica,martillo,pernos,cementos,tablas,sin_igv="",0.0,0.0,0.0,0.0,0.0,0.0
nombre_del_comprador=str(input("ingrese nombre:"))
puerta_acrilica=float(input("ingrese puerta acrilica:"))
martillo=float(input("ingrese martillo:"))
pernos=float(input("ingrese pernos:"))
cementos=float(input("ingrese cemento:"))
tablas=float(input("ingrese tabla:"))
sin_igv=float(input("ingrese sin igv:"))
#processing
t=(puerta_acrilica+martillo+pernos+cementos*2+tablas+sin_igv)
if(t > 32):
    print("iva incluido")
#fin_if
