# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
import logica_tarjeta 

# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def test_normal_1(self):
        # ENTRADAS
        compra = 200000
        interes = 3.1 / 100
        plazo = 36
        cuota = 9297.96
        #SALIDAS ESPERADAS
        total_abonos = 334_726.53
        total_intereses = 134_726.53

        cuota_calculada = logica_tarjeta.calcular_cuota( compra, interes, plazo )
        total_abonos_calculado = logica_tarjeta.calcular_total_abonos( compra, interes, plazo )
        total_intereses_calculado = logica_tarjeta.calcular_total_intereses( compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual( cuota, cuota_calculada, 2 )
        self.assertAlmostEqual( total_abonos, total_abonos_calculado, 2  )
        self.assertAlmostEqual( total_intereses, total_intereses_calculado, 2 )

    def test_normal_2(self):
        compra = 850000
        tasa = 3.4 / 100
        plazo = 24
        cuota = 52377.5
        resultado = logica_tarjeta.calcular_cuota( compra, tasa, plazo )
        self.assertEqual( cuota, round(resultado,2)  )

    def test_tasa_cero(self):
        # ENTRADAS
        compra = 480_000
        interes = 0 / 100
        plazo = 48
        #SALIDAS ESPERADAS
        cuota_esperada =10000
        total_abonos = 480_000
        total_intereses = 0

        cuota_calculada = logica_tarjeta.calcular_cuota( compra, interes, plazo )
        total_abonos_calculado = logica_tarjeta.calcular_total_abonos( compra, interes, plazo )
        total_intereses_calculado = logica_tarjeta.calcular_total_intereses( compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual( cuota_esperada, cuota_calculada, 2 )
        self.assertAlmostEqual( total_abonos, total_abonos_calculado, 2  )
        self.assertAlmostEqual( total_intereses, total_intereses_calculado, 2 )

    def test_compra_cero(self):
        # ENTRADAS
        compra = 0
        interes = 2.4 / 100
        plazo = 60
        #SALIDAS ESPERADAS

        # Verifica que si se genere una excepcion adentro del bloque with
        with self.assertRaises( logica_tarjeta.CompraInvalida ) :
            cuota_calculada = logica_tarjeta.calcular_cuota( compra, interes, plazo )

    def test_plazo_cero( self ):
        compra = 80000
        interes = 2.4 / 100
        plazo = 0

        # Verifica que si se genere una excepcion adentro del bloque with
        with self.assertRaises( logica_tarjeta.PlazoInvalido ) :
            cuota_calculada = logica_tarjeta.calcular_cuota( compra, interes, plazo )

    def test_usura( self ):
        compra = 80000
        interes = 12.4 / 100
        plazo = 60

        with self.assertRaises( logica_tarjeta.TasaExcesiva ):
            logica_tarjeta.calcular_cuota( compra, interes, plazo)


# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()