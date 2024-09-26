import pandas as pd

# Lee los archivos CSV que están en la carpeta "data"
csv1 = pd.read_csv('data/educacio.csv')  # Reemplaza 'archivo1.csv' con el nombre real
csv2 = pd.read_csv('data/sanitat.csv')  # Reemplaza 'archivo2.csv' con el nombre real

# Combina los dos CSV. Puedes usar concat si solo quieres unir los datos, o merge si tienes claves comunes
combined_csv = pd.concat([csv1, csv2], ignore_index=True)

# Guarda el CSV combinado
combined_csv.to_csv('data/archivo_combinado.csv', index=False)

print("CSV combinado guardado exitosamente!")
