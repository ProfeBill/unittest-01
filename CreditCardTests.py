# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
import Payment 


# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo de la clase
    def testPayment(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        compra = 200000
        tasa = 3.1
        plazo = 36
        cuota = 9297.96
        resultado = Payment.calcularCuota( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, resultado  )

# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    unittest.main()