num_a = input("Introduce un numero a")
num_b = input("Introduce otro numero b")
num_a = int(num_a)
num_b = int(num_b)
def sumar(num_a: int, num_b: int):
    print(f"Operacion suma:{num_a} + {num_b}")
    return num_a + num_b
def resta(num_a: int, num_b: int):
    print(f"Operacion resta:{num_a} - {num_b}")
    return num_a - num_b
def multiplicacion(num_a: int, num_b: int):
    print(f"Operacion multiplicacion:{num_a} * {num_b}")
    return num_a * num_b
def division(num_a: int, num_b: int):
    print(f"Operacion multiplicacion:{num_a} / {num_b}")
    return num_b / num_a
def modulo(num_a: int, num_b: int):
    print(f"Operacion multiplicacion:{num_b} %{num_a}")
    return num_a % num_b
def convertir_entero (variable):
    return int (variable)
def convertir_float (variable):
    return float (variable)

print(f"Resultado suma {sumar(num_a, num_b)}")
print(f"Resultado resta {resta(num_a, num_b)}")
print(f"Resultado multiplicacion{multiplicacion(num_a, num_b)}")
print(f"Resultado división {division(num_b, num_a)}")
print(f"Resultado Módulo {modulo(num_b, num_a)}")

