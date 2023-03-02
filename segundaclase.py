#Paso1: Pedirle al usuario el total de la factura
totalFactura = int(input("Por favor ingerese el valor total de la factura: "))

#Paso2: Pedirle al usuario el valor que quiere dar de propina
totalPropina = int(input("Por favor ingerese el valor que quiere dar de propina: "))

#Paso3: Hacer el calculo de la cuenta
totalCuenta = totalFactura + totalPropina

print(f"el valor total de la cuenta es: {totalCuenta} pesos")
