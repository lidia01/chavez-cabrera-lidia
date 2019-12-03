#ejercicio12
#declaracion de variables
nombre,primer_bimestre,segundo_bimestre,tercer_bimestre,cuarto_bimestre="",0,0,0,0
nombre=str(input("ingrese nombre:"))
primer_bimestre=int(input("ingrese primer bimestre:"))
segundo_bimestre=int(input("ingrese segundo bimestre:"))
tercer_bimestre=int(input("ingrese tercer bimestre:"))
cuarto_bimestre=int(input("ingrese cuarto bimestre:"))
#processing
promedio=(primer_bimestre+segundo_bimestre+tercer_bimestre+cuarto_bimestre)/4
if(promedio < 10):
    print("resprobo")
#fin_if
