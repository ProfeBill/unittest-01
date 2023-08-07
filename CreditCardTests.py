# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
import Payment 


# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def testPayment1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        compra = 200000
        tasa = 3.1
        plazo = 36
        cuota = 9297.96
        resultado = Payment.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def testPayment1_1(self):
        compra = 850000
        tasa = 3.4
        plazo = 24
        cuota = 52377.5
        resultado = Payment.calcularCuota( compra, tasa, plazo )
        self.assertEqual( cuota, round(resultado,2)  )

    def testPayment2(self):
        """ Compra normal con todos los parametros correctos """
        compra = 480000
        tasa = 0
        plazo = 48
        cuota = 10000

        resultado = Payment.calcularCuota( compra, tasa, plazo )

        self.assertEqual( cuota, round(resultado,2)  )


    def testPayment4(self):
        """  Compra a una sola cuota """
        compra = 90000
        tasa = 2.4
        plazo = 1
        cuota = 90000
        resultado = Payment.calcularCuota( compra, tasa, plazo )
        self.assertEqual( cuota, round(resultado,2)  )

    def testPayment3(self):
        """ Compra con tasa excesiva """
        compra = 50000
        tasa = 12.4
        plazo = 60
        
        try:
            resultado = Payment.calcularCuota( compra, tasa, plazo )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Payment.TasaExcesiva  :
            pass  # Forzar Exito

    def testPayment3_v2(self):
        """ Compra con tasa excesiva """
        compra = 50000
        tasa = 12.4
        plazo = 60
        # Para controlar que una funcion si genere una excepcion
        # en el caso de prueba, se usa el metodo assertRaises
        # el primer parametro es la Excepcion esperada
        # el segundo es el metodo que se va a invocar
        # y los demas parametros son los parametros del metodo bajo prueba
        self.assertRaises( Payment.TasaExcesiva,  Payment.calcularCuota, compra, tasa, plazo )

# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()