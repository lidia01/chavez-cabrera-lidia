#ejercicio19
#declaracion de variables
cantidad_de_trabajadores=0
horas_laboradas=0
cantidad_de_trabajadores=int(input("ingrese cantidad de trabajadores:"))
horas_laboradas=int(input("ingrese horas laboradas:"))
#processing
m=(cantidad_de_trabajadores*horas_laboradas)
if(m>95):
    print("sn quejas")
else:
    print("con quejas")
