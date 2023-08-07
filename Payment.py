def calcularCuota(compra,tasa,plazo):
    """
    Calcula la cuota a pagar por una compra con una tarjeta de crédito

    """

    """ La tasa de interés está expresada como un entero entre 1 y 100 """
    i =  tasa / 100
    return (compra * i) / (1 - (1 + i) ** (-plazo))

