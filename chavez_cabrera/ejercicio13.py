#ejercicio13
#declaracion de variables
nombre,dni,año_nacimiento,año_actual="","",0,0
nombre=str(input("ingrese nombre:"))
dni=str(input("ingrese dni:"))
año_nacimiento=int(input("año_nacimiento:"))
año_actual=int(input("año actual:"))
#processing
edad=(año_actual - año_nacimiento)
if(edad >= 22):
    print("mayor de edad")
#fin_if
