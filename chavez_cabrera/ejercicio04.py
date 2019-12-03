#ejercicio04
#declaracion de variables
nombre_del_solicitante,edad,ano_de_inscripcion,pago_mensual_por_cinco_años="",0,0,0.0
nombre_del_solicitante=str(input("ingrese nombre del solicitante:"))
edad=int(input("ingrese edad:"))
ano_de_inscripcion =int(input("ingrese ano de ingreso:"))
pago_mensual=float(input("ingrese pago mensual:"))
#processing
m=(pago_mensual*5)
if(m>81):
    print("calidad de servicio")
#fin_if
