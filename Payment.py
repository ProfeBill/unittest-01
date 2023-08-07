# Exepcion personalizada que se usa en un caso de error particular
class TasaExcesiva( Exception ): 
    pass

def calcularCuota(compra,tasa,plazo):
    """
    Calcula la cuota a pagar por una compra con una tarjeta de crédito
    compra : Valor de la compra con la tarjeta
    tasa : Debe ser un porcentaje entre 1 y 100
    plazo : numero de cuotas a diferir la compra

    El resultado no esta redondeado
    """

    if tasa*12 > 100 :
        """ Si la tasa anual es mayor que 100, arroja una excepcion """
        raise TasaExcesiva( "La tasa no debe ser superior a 100" )

    if plazo == 1 :
        """ Cuando el plazo sea una sola cuota, no se aplican intereses """
        return compra

    """ La tasa de interés está expresada como un entero entre 1 y 100 """
    i =  tasa / 100
 
    if tasa == 0:
        """ 
        Cuando la tasa sea cero, la cuota es la compra dividida las cuotas
        para evitar error de division por cero 
        """
        return compra / plazo
    else:         
        return (compra * i) / (1 - (1 + i) ** (-plazo))

