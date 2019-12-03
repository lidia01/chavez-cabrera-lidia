#ejercicio03
#declaracion de variables
nombre_del_paciente,paracetamol,diclofenaco,doloneurobion="",0.0,0.0,0.0
nombre_del_paciente=input("ingrese nombre del paciente:")
paracetamol=float(input("ingrese paracetamol:"))
diclofenaco=float(input("ingrese diclofenaco:"))
doloneurobion=float(input("ingrese doloneurobion:"))
#processing
m=(paracetamol+diclofenaco+doloneurobion)
if (m>120):
    print("costo pagado")
#fin_if
