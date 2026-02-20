import logica_tarjeta
"""
La interfaz de usuario del programa debe separarse del modulo 
que contiene la lógica.

En este caso, la interfaz de usuario queda en CreditCardConsole.py
y la lógica queda en Payment.py
"""
try:
    print("Este programa le permite calcular la cuota a pagar por una compra con tarjeta de credito")
    monto = float( input("Monto de la compra:") )

    if monto == 0 :
        print( "La compra debe ser mayor que cero")

    tasa = float( input("Tasa de interés de la tarjeta:") ) / 100
    plazo = float( input("Numero de cuotas en que va a diferir la compra:") )

    cuota = round( logica_tarjeta.calcular_cuota(monto,tasa,plazo) , 2)
    print( f"La cuota mensual a pagar es de: {cuota}"  )
except Exception as err:
    print("No se pudo calcular la cuota")
    print( str(err) )
