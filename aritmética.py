dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))

if divisor == 0:
    print("¡Error! No puedes dividir por cero.")
else:
    resultado = dividendo / divisor
    print(f"El resultado de dividir {dividendo} entre {divisor} es: {resultado}")