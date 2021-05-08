"""Sabes si es par o impar"""
Variable=17
if(Variable%2==0):
	print("Si es par")
else:
	print("Es impar")


"""Calculo de año biciesto o no"""
Año=2000
if(Año%4==0):
	print("Su año tiene 366 dias , por lo tanto",Año, "es biciesto")
else:
	print("Su año tiene 365 dias , por lo tanto",Año,"no es biciesto")


"""Interes compuesto e interes simple"""
P=1000 #monto a calcular el interes compuesto en Lempiras o la moneda que quieran
R=5 # este sera el % de interes sobre el cual se desea calcular "P"
T=3 # Periodo de tiempo en el cual se desea calcular el interes

ISimple=(P*R*T)/100
print("Su interes simple en",T,"años sera: L.",ISimple)

ICompuesto=(P*((1+R/100)**T-1))
print("Su interes compuesto en",T,"años sera: L.",ICompuesto)


