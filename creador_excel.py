# Importamos pandas para crear el excel 
import pandas as pd

# Cremos un diccionario para poner la informacion que queremos que aparezca en el excel
data = {
    "Piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centímetros":[40, 120, 60, 30, 180]
}

df = pd.DataFrame(data)

#Guardamos el dataframe en un archivo Excel

df.to_excel("Muebles_medidas.xlsx", index=False)