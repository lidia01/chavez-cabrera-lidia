#ejercicio17
#declaracion de variables
cliente,numero_de_tarjeta,polvo_compacto,rubor,labiales,aretes="","",0.0,0.0,0.0,0.0
cliente=str(input("cliente:"))
numero_de_tarjeta=str(input("numero de tarjeta:"))
polvo_compacto=float(input("ingrese polvo compacto:"))
rubor=float(input("ingrese rubor:"))
labiales=float(input("ingrese labial:"))
aretes=float(input("ingrese aretes:"))
#processing
t=(polvo_compacto+rubor+labiales+aretes*2)
if(t > 50):
    print("buen servicio")
#fin_if
