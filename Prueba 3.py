import csv
with open('listado.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

print("Contenido original del archivos CSV: ")
for row in rows:
    print(row)
    
def encontrar_saldo_mayor():
    saldo_mayor = 0
    for cliente in id:
        if cliente["saldo"] > encontrar_saldo_mayor:
            saldo_mayor = cliente["saldo"]
    return saldo_mayor

# Function to find the lowest balance
def encontrar_saldo_menor():
    saldo_menor = id[0]["saldo"]
    for cliente in id:
        if cliente["saldo"] < saldo_menor:
            saldo_menor = cliente["saldo"]
    return saldo_menor

# Function to calculate the average balance
def calcular_promedio_saldos():
    saldo_total = 0
    for cliente in id:
        saldo_total += cliente["saldo"]
    saldo_promedio = saldo_total / len(id)
    return saldo_promedio

   