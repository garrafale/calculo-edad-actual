from os import system
system ("cls")

from datetime import date

hoy=date.today()
dia_actual=hoy.day
mes_actual=hoy.month
año_actual=hoy.year

dia_nacimiento=int(input("Ingrese el día de nacimiento de la persona: "))
mes_nacimiento=int(input("Ingrese el mes de nacimiento de la persona: "))
año_nacimiento=int(input("Ingrese el año de nacimiento de la persona: "))

print()

if dia_nacimiento>31 or dia_nacimiento <1 or mes_nacimiento<1 or mes_nacimiento>12:
	print("Algún dato está mal ingresado")
elif dia_nacimiento==31 and (mes_nacimiento==2 or mes_nacimiento==4 or mes_nacimiento==6 or mes_nacimiento==9 or mes_nacimiento==11):
	print("Algún dato está mal ingresado")
elif dia_nacimiento==30 and mes_nacimiento==2:
	print("Algún dato está mal ingresado")
elif dia_nacimiento==29 and mes_nacimiento==2 and (año_nacimiento%4 !=0 or (año_nacimiento%100==0 and año_nacimiento%400!=0)):
	print("Algún dato está mal ingresado")
else:
	edad=año_actual-año_nacimiento

	if mes_actual<mes_nacimiento:
		edad-=1
	elif mes_actual==mes_nacimiento:
		if dia_actual < dia_nacimiento:
			edad-=1

	if edad>=0:
		if edad==0:
			print("La persona en cuestión todavía no ha cumplido años")
		elif edad==1:
			print("La persona en cuestión tiene 1 año")
		else:
			print("La persona en cuestión tiene",edad,"años")
	if edad<0:
		print("Algún dato está mal ingresado")
