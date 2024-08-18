# importamos pandas 
import pandas as pd

# creamos una funcion que convierta de cm a pulgadas
def cm_pulgadas(cm):
    return cm / 2.54

# leemos el archivo excel que creamos antes
df = pd.read_excel("Muebles_medidas.xlsx")

# añadimos una columna con los datos de las pulgadas al archivo Excel

df["Pulgadas"] = df["Centímetros"].apply(cm_pulgadas)

df.to_excel("Muebles_medidas_convertidas.xlsx", index=False)

print("el archivo excel ha sido creado y leido correctamente lo puedes ver en el archivo: 'Muebles_medidas_convertidas.xlsx'", )