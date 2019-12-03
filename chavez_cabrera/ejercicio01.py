#ejercicio01
#declaracion de variables
neumaticos,armadura_doble,fibra_de_carbono,cadena_unitaria=0.0,0.0,0.0,0.0
neumaticos=float(input("ingrese neumaticos:"))
armadura_doble=float(input("ingrese armadura doble:"))
fibra_de_carbono=float(input("ingrese fibra de carbono:"))
cadena_unitaria=float(input("ingrese cadena unitaria:"))
#processing
total_a_pagar=(neumaticos+armadura_doble+fibra_de_carbono+cadena_unitaria)
comprador_impulsivo=(total_a_pagar > 100)
if(comprador_impulsivo):
    print("comprador impulsivo")
else:
    print("no es comprador impulsivo")


















































