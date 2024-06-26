import csv
with open('listado.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

print("Contenido original del archivos CSV: ")
for row in rows:
    print(row)