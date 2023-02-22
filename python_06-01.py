#Puede subir o no a la montaña rusa
edad = input("Introduce TU EDAD")
estatura = input("Introduce tu estatura")
edad = int(edad)
estatura = float(estatura)

# si mas mayor a 14 años  y tiene una altura no menor de 1,62. El script debe ser
# capaz de informar si puede
# o no subirse y en el caso de que no, porque razon (Si por edad, por tamaño u ambas)




if (edad >14 and estatura >=1.62):
    print("se sube a la montaña rusa")
elif (edad <=14 and estatura >=1.62):
    print("No puede subirse por que es menor de 14 años de edad")
elif (edad > 14 and estatura <=1.62):
    print("No puede subir a la montana rusa, ya que mide menos de 1.62 ")