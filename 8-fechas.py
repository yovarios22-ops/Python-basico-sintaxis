#yovani.Z
#fechas en python 

from datetime import date, datetime

#Fecha actual 
hoy = date.today()
print(hoy)

#formatear fecha (formato)
formateado = hoy.strftime("%d/%m/%Y")
print(formateado)

#hora actual
fecha_actual = datetime.now()
print(fecha_actual)

#capturar el año 
anio = fecha_actual.year
print(anio)
#mes
mes = fecha_actual.month
print(mes)
#dia 
dia = fecha_actual.day
print(dia)

hora_actual = fecha_actual.strftime("%H:%M:%S")
print(hora_actual)

#formato AM, PM
hora_am_pm = fecha_actual.strftime("%I:%M:%S %p")
print(hora_am_pm)
