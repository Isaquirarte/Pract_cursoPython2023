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

año_nacimiento = input("Introduce tu año de Nacimiento")
año_nacimiento = int(año_nacimiento)
mes= input("introduce tu mes de nacimiento")
mes= int(mes)
dia= input("introduce tu dia de nacimiento")
dia= int(dia)
año_actual = 2023
mes_actual= 2
mes_actual = int(mes_actual)
dia_actual = 21

años = año_actual - año_nacimiento
print(f"tu edad es:{años }")

cumpleaños = (mes>= mes_actual )and (dia >= dia_actual)
print(f"cumpleaños: {cumpleaños}")

#------GENERACIONES----

"""Determinar a qué generación pertenece:"""

if año_nacimiento <= 1939:
    print("La generación silenciosa. Nacidos entre 1920 y 1939.")
elif año_nacimiento <=1959:
    print("Los baby boomers. Nacidos entre 1940 y 1959.")
elif año_nacimiento <=1979:
    print("Generación X. Nacidos entre 1960 y 1979.")
elif año_nacimiento <=1989:
    print("Generación Y o millennials. Nacidos entre 1980 y 1989.")
else:
     print("Generación Z. Nacidos entre 1990 en adelante.")
