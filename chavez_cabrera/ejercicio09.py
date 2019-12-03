#ejercicio9
#declaracion de variables
nombre_del_libro,nro_de_hojas,precio_por_hoja="",0,0.0
nombre_del_libro=str(input("ingrese nombre del libro:"))
nro_de_hojas=int(input("ingrese nro de hojas:"))
precio_por_hoja=float(input("ingrese precio por hoja:"))
#processing
t=(nro_de_hojas*precio_por_hoja)
if(t > 20):
    print("buen servicio")
#fin_if
