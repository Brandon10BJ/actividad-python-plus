#b
import pandas as pd
from pathlib import Path

file_route = Path('.') / 'dataset' / 'area_protegida.csv'
# Leer el archivo CSV
df = pd.read_csv(file_route)
# Calcular el valor promedio de la columna 13
value_data = df.iloc[:, 13].mean()

# Filtrar los datos usando pandas y apply
filtered_data1 = df[df.iloc[:, 8].apply(lambda x: x in [1, 2]) & (df.iloc[:, 13] < value_data)]
filtered_data2 = df[df.iloc[:, 8].apply(lambda x: x == 3) & (df.iloc[:, 13] < value_data)]

#values  contiene los valores de todas las filas y columnas
#lo pasamos a tipo list
lista1 = list(filtered_data1.values)
lista2 = list(filtered_data2.values)

print('punto b')
print(len(lista1))
print(f"\n****\n{len(lista2)}")


#c------------------
# Crear una Serie a partir de los datos agrupados
grouped_data=df.groupby(df.columns[8])[df.columns[13]].sum()
serie = pd.Series(grouped_data.values, index=grouped_data.index, name='Serie_Agrupada')
    
# Imprimir la Serie creada
print('punto c')
print("Serie creada:")
print(serie)
    
# Crear un DataFrame a partir del DataFrame original
columns_to_include = [0,1,6,7]  # incluimos las columnas 0, 1, 8 y 13
new_df = df.iloc[:, columns_to_include].head(5)# mostramos los primeros 5

#iloc[:, columns_to_include]:
#iloc[]: Es un método de pandas que permite la indexación basada en la ubicación.
#[...]: Dentro de iloc[], el primer conjunto de corchetes ([]) se refiere a la selección de filas y el segundo conjunto se refiere a la selección de columnas.
#: antes de la coma (:): Esto indica que queremos seleccionar todas las filas del DataFrame.
#columns_to_include después de la coma (:): Esto especifica las columnas que deseamos seleccionar.
# Imprimir el DataFrame creado
print("\nDataFrame creado:")
print(new_df.head())


#d----------
print('punto d')
print(df.dtypes)

#e--------------
# ventaja 1
# Con Pandas, puedes limpiar y transformar tus datos fácilmente. Puedes eliminar filas o columnas duplicadas, manejar valores nulos y 
# filtrar tus datos de forma sencilla. 

# ventaja 2
# Con pandas, no estás limitado a trabajar solo con archivos CSV. La librería proporciona métodos para leer y escribir datos en una variedad
# de formatos, incluyendo Excel, HDF5, SQL, JSON, HTML, entre otros, lo que nos brinda ms flexibilidad. 

# ventaja 3
# Pandas está optimizado para el manejo de datos en memoria y utiliza estructuras de datos eficientes, como DataFrames y Series, 
# que permiten realizar operaciones vectorizadas y paralelizadas en los datos. Esto significa que pueden hacer operaciones de limpieza, 
# transformación y análisis en conjuntos de datos grandes de manera rápida y eficiente, sin tener que preocuparte por problemas de rendimiento o 
# limitaciones de memoria.