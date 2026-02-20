# Exepcion personalizada que se usa en un caso de error particular
class TasaExcesiva( Exception ): 
    pass

def calcular_cuota(compra,tasa,plazo):
    """
    Calcula la cuota a pagar por una compra con una tarjeta de crédito
    compra : Valor de la compra con la tarjeta
    tasa : Debe ser un porcentaje entre 1 y 100
    plazo : numero de cuotas a diferir la compra

    El resultado no esta redondeado
    """
    if compra == 0 :
    #### RETORNAR UN ERROR
        raise Exception("El valor de la compra debe ser mayor que cero")
 
    if tasa == 0:
        """ 
        Cuando la tasa sea cero, la cuota es la compra dividida las cuotas
        para evitar error de division por cero 
        """
        return compra / plazo
    else:         
        return (compra * tasa) / (1 - (1 + tasa) ** (-plazo))


def calcular_total_abonos(compra,tasa,plazo):
    cuota = calcular_cuota( compra, tasa, plazo)
    return cuota * plazo

def calcular_total_intereses(compra,tasa,plazo):
    total_abonos = calcular_total_abonos( compra, tasa, plazo)
    return total_abonos - compra