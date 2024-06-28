import csv
import time
import random

def generar_saldo_aleatorio():
  """Genera un saldo aleatorio entre 1000 y 100000."""
  return random.randint(1000, 100000)

# Crear una lista de clientes
clientes = [
    {"nombre": "Cliente 1", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 2", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 3", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 4", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 5", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 6", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 7", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 8", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 9", "saldo": generar_saldo_aleatorio()},
    {"nombre": "Cliente 10", "saldo": generar_saldo_aleatorio()},
]

# Escribir datos de clientes en un archivo SSV
with open("datos_clientes.csv", "w") as f:
    for cliente in clientes:
        f.write(f"{cliente['nombre']},{cliente['saldo']}\n")

def encontrar_saldo_mayor():
  """Encuentra el saldo más alto entre los clientes."""
  saldo_mayor = 0
  for cliente in clientes:
    if cliente["saldo"] > saldo_mayor:
      saldo_mayor = cliente["saldo"]
  return saldo_mayor

def encontrar_saldo_menor():
  """Encuentra el saldo más bajo entre los clientes."""
  saldo_menor = clientes[0]["saldo"]
  for cliente in clientes:
    if cliente["saldo"] < saldo_menor:
      saldo_menor = cliente["saldo"]
  return saldo_menor

def calcular_promedio_saldos():
  """Calcula el promedio de saldos de todos los clientes."""
  saldo_total = 0
  for cliente in clientes:
    saldo_total += cliente["saldo"]
  saldo_promedio = saldo_total / len(clientes)
  return saldo_promedio

# Interfaz de usuario para interactuar con la aplicación
while True:
    print("\n**Servicio de administración de cuentas**")
    print("1. Listado de clientes")
    print("2. Saldo más alto")
    print("3. Saldo más bajo")
    print("4. Calcular promedio de saldos")
    print("5. Salir")

    opcion = input("Ingrese su opción (1-5): ")

    if opcion == "1":
        # Mostrar datos de clientes desde el archivo SSV
        with open("datos_clientes.csv", "r") as f:
            for line in f:
                nombre, saldo = line.strip().split(",")
                print(f"Nombre: {nombre}, Saldo: {saldo}")

    elif opcion == "2":
        saldo_mayor = encontrar_saldo_mayor()
        print(f"El saldo más alto es: {saldo_mayor}")

    elif opcion == "3":
        saldo_menor = encontrar_saldo_menor()
        print(f"El saldo más bajo es: {saldo_menor}")

    elif opcion == "4":
        saldo_promedio = calcular_promedio_saldos()
        print(f"El promedio de saldos es: {saldo_promedio}")

    elif opcion == "5":
        print("Finalizando...")
        break

    else:
        print("Opción inválida. Seleccione una opción entre 1 y 5.")
   