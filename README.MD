# Mi primera prueba unitaria

Este proyecto contiene la prueba unitaria más básica que puede crearse en Python
para ser usada como un modelo para crear nuevas pruebas.

Solo para probar ocmo hacer un PR

## Contenido

### CreditCardTests.py


Implementa las siguientes pruebas unitarias:

Compra Normal 1
	Entradas
		Compra: 200.000
		Tasa: 3.1% mensual
		Plazo: 36
	Salidas
		Cuota: 9.297.96

Casos Normal 1.1
	Entradas
		Compra: 850.000
		Tasa: 3.4% mensual
		Plazo: 24
	Salidas
		Cuota: 52377.50

	Caso 2
		Entradas
			Compra: 480.000
			Tasa: 0% mensual
			Periodos: 48
		Salidas
			Pago: 10.000
	Caso 4
		Entradas
			Monto: 90000
			Tasa: 2.4%
			Plazo :1
		Salidas
			90.000
	Caso 3
		Entradas
			Monto: 50.000
			Tasa: 12.4%
			Cuotas: 60
		Salidas
			Error: La tasa no puede superar el 100% anual

### Payment.py

Implementa la funcionalidad que cumple con estos casos
