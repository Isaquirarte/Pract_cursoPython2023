"""Escribe un script que dado el día,mes y año de nacimiento de una persona determine lo siguiente:

Cuántos años tiene.
Si en lo que va del año ya cumplio o no.
Determinar a qué generación pertenece:
La generación silenciosa. Nacidos entre 1920 y 1939.
Los baby boomers. Nacidos entre 1940 y 1959.
Generación X. Nacidos entre 1960 y 1979.
Generación Y o millennials. Nacidos entre 1980 y 1989.
Generación Z. Nacidos entre 1990 en adelante.
Extra: Utilizar libreria de datetime para obtener mes y año."""

año_nacimiento = input("Introduce TU fecha de Nacimiento")
mes= input("introduce tu mes de nacimiento")
dia= input("introduce tu dia de nacimiento")
actual = 2023
#actual= float(actual)
mes_actual = 2
resta = actual -año_nacimiento

print(f"{resta }")