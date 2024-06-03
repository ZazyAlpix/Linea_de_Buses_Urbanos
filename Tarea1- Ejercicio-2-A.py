# Integrantes: Alejandro Narváez. 
# RUT        : 26.286.781-1

# PREGUNTA 2: Hacemos sistema para elegir destino, luego la cantidad de maletas y por último la muestra gráfica

print("Bienvenido a la Línea de Buses Interurbanos")

print("1. Santiago   : $18.000 por tramo")
print("2. Arica      : $18.500 por tramo")
print("3. Temuco     : $20.580 por tramo")
print("4. Concepción : $18.600 por tramo")
# Cantidad de Viajes:
viaje_santiago = 0
viaje_arica = 0
viaje_temuco = 0
viaje_concepcion = 0

#precios:
precio_santiago = 18000
precio_arica = 18500
precio_temuco = 20580
precio_concepcion = 18600

valor_total_pasaje_santiago = 0
valor_total_pasaje_arica = 0
valor_total_pasaje_temuco = 0
valor_total_pasaje_concepcion = 0


#Lista para viajes repetidos:

destino = int(input("Seleccione un destino (1,2,3,4): "))
if destino ==1:
   viaje_santiago +=1
   valor_total_pasaje_santiago += 18000
   destino_si_no = str(input(f"¿Desea el pasaje de Santiago de vuelta tambien? (si/no): "))
   if destino_si_no.lower() == "si":
    print(f"Su pasaje a Santiago será de {precio_santiago * 2} $.")
    valor_total_pasaje_santiago +=18000
   else:
     print(f"Su pasaje de Santiago será de {precio_santiago} $.")
elif destino ==2:
  viaje_arica +=1
  valor_total_pasaje_arica +=18500
  destino_si_no = str(input(f"¿Desea el pasaje de Arica de vuelta tambien? (si/no): "))
  if destino_si_no.lower() == "si":
    print(f"Su pasaje a Arica será de {precio_arica * 2} $.")
    valor_total_pasaje_arica += 18500
  else:
     print(f"Su pasaje a Arica será de {precio_arica} $.")

elif destino ==3:
  viaje_temuco +=1
  valor_total_pasaje_temuco += 20580
  destino_si_no = str(input(f"¿Desea el pasaje de Temuco de vuelta tambien? (si/no): "))
  if destino_si_no.lower() == "si":
    print(f"Su pasaje a Temuco será de {precio_arica * 2} $.")
    valor_total_pasaje_temuco += 20580
  else:
    print(f"Su pasaje a Temuco será de {precio_temuco} $")

elif destino ==4:
  viaje_concepcion +=1
  valor_total_pasaje_concepcion += 18600
  destino_si_no =str(input(f"¿Desea el pasaje de Concepción de vuelta también? (si/no): "))
  if destino_si_no.lower() == "si":
    print(f"Su pasaje a Concepción será de {precio_concepcion * 2} $.")
    valor_total_pasaje_concepcion += 18600
  else:
    print(f" Su pasaje a Concepción será de {precio_concepcion} $.")
else:
  print("error.")

#Cantidad de Maletas:
valor_total_maletas = 0
cantidad_maletas = 0
cantidad_maletas += int(input("¿Cuántas maletas llevará para el viaje?:"))
if cantidad_maletas >=2:
  print(f"El valor de su equipaje será de {(cantidad_maletas - 1) * 5000} $")

elif cantidad_maletas <0:
  print("error")

elif cantidad_maletas ==1:
  print("Si lleva 1 maleta su costo de equipaje será de 0 $")

elif cantidad_maletas ==0:
  print("Si no lleva maletas su costo de equipaje será de 0 $")

else:
  print("error.")

valor_total_maletas += (cantidad_maletas - 1) * 5000

#Muestra de Boleto:
if destino ==1:
  muestra_destino = "SANTIAGO"

if destino ==2:
  muestra_destino = "ARICA"

if destino ==3:
  muestra_destino = "TEMUCO"

if destino ==4:
  muestra_destino = "CONCEPCION"

if destino_si_no == "si":
  muestra_santiago = "ida y vuelta"
else:
  muestra_santiago = "ida"

if destino_si_no == "si":
  muestra_arica = "ida y vuelta"
else:
  muestra_arica = "ida"

if destino_si_no == "si":
  muestra_temuco = "ida y vuelta"
else:
  muestra_temuco = "ida"

if destino_si_no == "si":
  muestra_concepcion = "ida y vuelta"
else:
  muestra_concepcion = "ida"

#Valores ida y vuelta:

if destino_si_no == "si":
  destino_ida_y_vuelta = "ida y vuelta"
  muestra_valor_santiago = 36000
else:
  muestra_valor_santiago = precio_santiago
  destino_ida_y_vuelta ="ida"

if destino_si_no == "si":
  destino_ida_y_vuelta = "ida y vuelta"
  muestra_valor_arica = 37000
else:
  muestra_valor_arica = precio_arica
  destino_ida_y_vuelta ="ida"

if destino_si_no == "si":
  destino_ida_y_vuelta = "ida y vuelta"
  muestra_valor_temuco = 41160
else:
  muestra_valor_temuco = precio_temuco
  destino_ida_y_vuelta ="ida"

if destino_si_no == "si":
  destino_ida_y_vuelta = "ida y vuelta"
  muestra_valor_concepcion = 37200
else:
  muestra_valor_concepcion = precio_concepcion
  destino_ida_y_vuelta ="ida"

#Valores de Destinos En Pantalla:
if muestra_destino == "SANTIAGO" and destino_ida_y_vuelta == "ida y vuelta":
  muestra_valor = 36000
  
elif muestra_destino == "SANTIAGO" and destino_ida_y_vuelta == "ida":
  muestra_valor = 18000

if muestra_destino == "ARICA" and destino_ida_y_vuelta == "ida y vuelta":
  muestra_valor = 37000
elif muestra_destino == "ARICA" and destino_ida_y_vuelta == "ida":
  muestra_valor = 18500

if muestra_destino == "TEMUCO" and destino_ida_y_vuelta == "ida y vuelta":
  muestra_valor = 41160
elif muestra_destino == "TEMUCO" and destino_ida_y_vuelta == "ida":
  muestra_valor = 20580

if muestra_destino == "CONCEPCION" and destino_ida_y_vuelta == "ida y vuelta":
  muestra_valor = 37200
elif muestra_destino == "CONCEPCION" and destino_ida_y_vuelta == "ida":
  muestra_valor = 18600

#Valor de Cantidad de Maletas:
if cantidad_maletas >= 2:
    muestra_valor_cantidad_maletas = (cantidad_maletas -1) * 5000
elif cantidad_maletas == 1:
  muestra_valor_cantidad_maletas = 0
elif cantidad_maletas == 0:
  muestra_valor_cantidad_maletas = 0

# MUESTRA VALOR TOTAL:
if muestra_destino == "SANTIAGO" and destino_ida_y_vuelta == "ida y vuelta":
  muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas 
  
elif muestra_destino == "SANTIAGO" and destino_ida_y_vuelta == "ida":
  muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

if muestra_destino == "ARICA" and destino_ida_y_vuelta == "ida y vuelta":
  muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

elif muestra_destino == "ARICA" and destino_ida_y_vuelta == "ida":
  muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

if muestra_destino == "TEMUCO" and destino_ida_y_vuelta == "ida y vuelta":
  muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

elif muestra_destino == "TEMUCO" and destino_ida_y_vuelta == "ida":
  muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

if muestra_destino == "CONCEPCION" and destino_ida_y_vuelta == "ida y vuelta":
  muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

elif muestra_destino == "CONCEPCION" and destino_ida_y_vuelta == "ida":
  muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

#MUESTRA GRÁFICA:
print(f"************PASAJE INTERURBANOS************")
print(f"Destino: {muestra_destino} {destino_ida_y_vuelta} Valor$ {muestra_valor}")
print(f"Unidades de Equipaje:{cantidad_maletas} Valor ${muestra_valor_cantidad_maletas}")
print(f"TOTAL: {muestra_valor_total}")

#Volver a iniciar el programa:

#Lista para viajes repetidos:


volver_a_iniciar = input("¿Desea volver a comprar un boleto?")

while volver_a_iniciar.lower() == "si":
    print("Bienvenido a la Línea de Buses Interurbanos")

    print("1. Santiago   : $18.000 por tramo")
    print("2. Arica      : $18.500 por tramo")
    print("3. Temuco     : $20.580 por tramo")
    print("4. Concepción : $18.600 por tramo")

    #precios:
    precio_santiago = 18000
    precio_arica = 18500
    precio_temuco = 20580
    precio_concepcion = 18600
    
    # Cantidad de Viajes:
    viaje_santiago += 0
    viaje_arica += 0
    viaje_temuco += 0
    viaje_concepcion += 0  

    
    destino = int(input("Seleccione un destino (1,2,3,4): "))
    if destino ==1:
      viaje_santiago +=1
      valor_total_pasaje_santiago += 18000
      destino_si_no = str(input(f"¿Desea el pasaje de Santiago de vuelta tambien? (si/no): "))
      if destino_si_no.lower() == "si":
        print(f"Su pasaje a Santiago será de {precio_santiago * 2} $.")
        valor_total_pasaje_santiago += 18000
      else:
        print(f"Su pasaje de Santiago será de {precio_santiago} $.")
    elif destino ==2:
      viaje_arica +=1
      valor_total_pasaje_arica += 18500
      destino_si_no = str(input(f"¿Desea el pasaje de Arica de vuelta tambien? (si/no): "))
      if destino_si_no.lower() == "si":
        print(f"Su pasaje a Arica será de {precio_arica * 2} $.")
        valor_total_pasaje_arica += 18500
      else:
        print(f"Su pasaje a Arica será de {precio_arica} $.")

    elif destino ==3:
      viaje_temuco +=1
      valor_total_pasaje_temuco += 20580
      destino_si_no = str(input(f"¿Desea el pasaje de Temuco de vuelta tambien? (si/no): "))
      if destino_si_no.lower() == "si":
        print(f"Su pasaje a Temuco será de {precio_arica * 2} $.")
        valor_total_pasaje_temuco += 20580
      else:
        print(f"Su pasaje a Temuco será de {precio_temuco} $")

    elif destino ==4:
      viaje_concepcion +=1
      valor_total_pasaje_concepcion += 18600
      destino_si_no =str(input(f"¿Desea el pasaje de Concepción de vuelta también? (si/no): "))
      if destino_si_no.lower() == "si":
        print(f"Su pasaje a Concepción será de {precio_concepcion * 2} $.")
        valor_total_pasaje_concepcion += 18600
      else:
        print(f" Su pasaje a Concepción será de {precio_concepcion} $.")
    else:
      print("error.")

    #Cantidad de Maletas:
    valor_total_maletas += 0
    cantidad_maletas = 0

    cantidad_maletas = int(input("¿Cuántas maletas llevará para el viaje?:"))
    if cantidad_maletas >=2:
      print(f"El valor de su equipaje será de {(cantidad_maletas - 1) * 5000} $")

    elif cantidad_maletas <0:
      print("error")

    elif cantidad_maletas ==1:
      print("Si lleva 1 maleta su costo de equipaje será de 0 $")

    elif cantidad_maletas ==0:
      print("Si no lleva maletas su costo de equipaje será de 0 $")

    else:
      print("error.")
    
    valor_total_maletas += (cantidad_maletas - 1) * 5000

    #Muestra de Boleto:
    if destino ==1:
      muestra_destino = "SANTIAGO"

    if destino ==2:
      muestra_destino = "ARICA"

    if destino ==3:
      muestra_destino = "TEMUCO"

    if destino ==4:
      muestra_destino = "CONCEPCION"

    if destino_si_no == "si":
      muestra_santiago = "ida y vuelta"
    else:
      muestra_santiago = "ida"

    if destino_si_no == "si":
      muestra_arica = "ida y vuelta"
    else:
      muestra_arica = "ida"

    if destino_si_no == "si":
      muestra_temuco = "ida y vuelta"
    else:
      muestra_temuco = "ida"

    if destino_si_no == "si":
      muestra_concepcion = "ida y vuelta"
    else:
      muestra_concepcion = "ida"

    #Valores ida y vuelta:

    if destino_si_no == "si":
      destino_ida_y_vuelta = "ida y vuelta"
      muestra_valor_santiago = 36000
    else:
      muestra_valor_santiago = precio_santiago
      destino_ida_y_vuelta ="ida"

    if destino_si_no == "si":
      destino_ida_y_vuelta = "ida y vuelta"
      muestra_valor_arica = 37000
    else:
      muestra_valor_arica = precio_arica
      destino_ida_y_vuelta ="ida"

    if destino_si_no == "si":
      destino_ida_y_vuelta = "ida y vuelta"
      muestra_valor_temuco = 41160
    else:
      muestra_valor_temuco = precio_temuco
      destino_ida_y_vuelta ="ida"

    if destino_si_no == "si":
      destino_ida_y_vuelta = "ida y vuelta"
      muestra_valor_concepcion = 37200
    else:
      muestra_valor_concepcion = precio_concepcion
      destino_ida_y_vuelta ="ida"

    #Valores de Destinos En Pantalla:
    if muestra_destino == "SANTIAGO" and destino_ida_y_vuelta == "ida y vuelta":
      muestra_valor = 36000
      
    elif muestra_destino == "SANTIAGO" and destino_ida_y_vuelta == "ida":
      muestra_valor = 18000

    if muestra_destino == "ARICA" and destino_ida_y_vuelta == "ida y vuelta":
      muestra_valor = 37000
    elif muestra_destino == "ARICA" and destino_ida_y_vuelta == "ida":
      muestra_valor = 18500

    if muestra_destino == "TEMUCO" and destino_ida_y_vuelta == "ida y vuelta":
      muestra_valor = 41160
    elif muestra_destino == "TEMUCO" and destino_ida_y_vuelta == "ida":
      muestra_valor = 20580

    if muestra_destino == "CONCEPCION" and destino_ida_y_vuelta == "ida y vuelta":
      muestra_valor = 37200
    elif muestra_destino == "CONCEPCION" and destino_ida_y_vuelta == "ida":
      muestra_valor = 18600

    #Valor de Cantidad de Maletas:
    if cantidad_maletas >= 2:
        muestra_valor_cantidad_maletas = (cantidad_maletas -1) * 5000
    elif cantidad_maletas == 1:
      muestra_valor_cantidad_maletas = 0
    elif cantidad_maletas == 0:
      muestra_valor_cantidad_maletas = 0

    # MUESTRA VALOR TOTAL:
    if muestra_destino == "SANTIAGO" and destino_ida_y_vuelta == "ida y vuelta":
      muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas 
      
    elif muestra_destino == "SANTIAGO" and destino_ida_y_vuelta == "ida":
      muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

    if muestra_destino == "ARICA" and destino_ida_y_vuelta == "ida y vuelta":
      muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

    elif muestra_destino == "ARICA" and destino_ida_y_vuelta == "ida":
      muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

    if muestra_destino == "TEMUCO" and destino_ida_y_vuelta == "ida y vuelta":
      muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

    elif muestra_destino == "TEMUCO" and destino_ida_y_vuelta == "ida":
      muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

    if muestra_destino == "CONCEPCION" and destino_ida_y_vuelta == "ida y vuelta":
      muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas

    elif muestra_destino == "CONCEPCION" and destino_ida_y_vuelta == "ida":
      muestra_valor_total = muestra_valor + muestra_valor_cantidad_maletas 
    volver_a_iniciar = input("¿Desea volver a comprar un boleto?")
    if volver_a_iniciar.lower() == "no":
      print(f"*************PASAJE INTERURBANOS*****************")
      print(f"Resumen de Ventas del día")
      print(f"Santiago: {viaje_santiago}")
      print(f"Arica: {viaje_arica}")
      print(f"Temuco: {viaje_temuco}")
      print(f"Concepción : {viaje_concepcion}")
      print(f"TOTAL EN PASAJES: ${valor_total_pasaje_santiago + valor_total_pasaje_arica + valor_total_pasaje_temuco + valor_total_pasaje_concepcion} ")
      print(f"TOTAL EN MALETAS: ${valor_total_maletas}")
      break
else:
    print(f"*************PASAJE INTERURBANOS*****************")
    print(f"Resumen de Ventas del día")
    print(f"Santiago: {viaje_santiago}")
    print(f"Arica: {viaje_arica}")
    print(f"Temuco: {viaje_temuco}")
    print(f"Concepción : {viaje_concepcion}")
    print(f"TOTAL EN PASAJES: ${valor_total_pasaje_santiago + valor_total_pasaje_arica + valor_total_pasaje_temuco + valor_total_pasaje_concepcion} ")
    print(f"TOTAL EN MALETAS: ${valor_total_maletas}")