#ejercicio36
#declaracion de variables
numero_de_cuenta_corriente=""
costo_por_giro=0.0
monto=0.0
numero_de_cuenta_corriente=str(input("ingrese numero de cuenta corriente:"))
costo_por_giro=float(input("ingrese costo por giro:"))
monto=float(input("ingrese monto:"))
#processing
total=(costo_por_giro*monto)
if(total<22):
    print("entregado a cuenta")
#fin_if



