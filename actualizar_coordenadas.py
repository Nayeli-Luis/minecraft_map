# Actualizar las coordenadas del mapa

import pandas as pd

print("====Registro de coordenadas Minecraft=====")

flag = input("Elige una opición: \n 1. Registrar coordenadas \n 2. Terminar: ")
flag = int(flag)

# convertir cada columna del dataframe a una lista
z_list = c["z"].tolist()
x_list = c["x"].tolist()
y_list = c["y"].tolist()
tipo_list = c["tipo_lugar"].tolist()
notas_list = c["notas"].tolist()

while flag != 2:
    x = float(input("Ingrese la coordenada x: "))
    z = float(input("Ingrese la coordenada z: "))
    y = float(input("Ingrese la coordenada y: "))
    tipo_lugar = str(input("Escriba el tipo de lugar: "))
    notas = input("Escribe notas: ")

    x_list.append(x)
    z_list.append(z) 
    y_list.append(y)
    tipo_list.append(tipo_lugar)
    notas_list.append(notas)

    flag = input("Comienza el registro, elige una opición: \n 1. Continuar \n 2. Terminar: ")
    flag = int(flag)
    
# Crear dataframe
print(x_list)
coord_df = pd.DataFrame(list(zip(x_list, z_list, y_list, tipo_list, notas_list)),
                       columns = ["x", "z", "y", "tipo_lugar", "notas"])

print(coord_df.head())

# Exportar dataset
coord_df.to_csv("coordenadas.csv")