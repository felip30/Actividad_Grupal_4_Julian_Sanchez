# Actividad_Grupal_4_Julian_Sanchez
# -------------------------------------------
# 0. Importar librerías
# -------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------
# 1. Crear los datos
# -------------------------------------------
datos = {
    "Mes": [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ],
    "Portatiles": [20, 18, 25, 30, 28, 35, 40, 38, 36, 34, 32, 30],
    "Monitores": [15, 16, 14, 18, 20, 22, 24, 23, 21, 19, 18, 17],
    "Teclados": [40, 42, 38, 45, 47, 50, 55, 53, 52, 48, 46, 44]
}

df = pd.DataFrame(datos)

# -------------------------------------------
# 2. Exploración básica
# -------------------------------------------
print("Primeras filas:")
print(df.head())

print("\nInformación del DataFrame:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

# -------------------------------------------
# 3. Estadísticas con NumPy
# -------------------------------------------
ventas_port = df["Portatiles"].values
ventas_mon = df["Monitores"].values
ventas_tec = df["Teclados"].values

print("\n=== Estadísticas adicionales ===")

print("\n--- Portátiles ---")
print("Media:", np.mean(ventas_port))
print("Mediana:", np.median(ventas_port))
print("Desviación estándar:", np.std(ventas_port))

print("\n--- Monitores ---")
print("Media:", np.mean(ventas_mon))
print("Mediana:", np.median(ventas_mon))
print("Desviación estándar:", np.std(ventas_mon))

print("\n--- Teclados ---")
print("Media:", np.mean(ventas_tec))
print("Mediana:", np.median(ventas_tec))
print("Desviación estándar:", np.std(ventas_tec))

# -------------------------------------------
# 4. Calcular total mensual
# -------------------------------------------
df["Total_Mensual"] = df["Portatiles"] + df["Monitores"] + df["Teclados"]

print("\nDataFrame con Total Mensual:")
print(df)

# -------------------------------------------
# 5. Mes con mayor venta total
# -------------------------------------------
mes_max = df.loc[df["Total_Mensual"].idxmax()]
print("\nMes con mayores ventas totales:")
print(mes_max)

# -------------------------------------------
# 6. GRÁFICOS
# -------------------------------------------

# Gráfico de líneas
plt.figure(figsize=(12,5))
plt.plot(df["Mes"], df["Portatiles"], marker="o", label="Portátiles")
plt.plot(df["Mes"], df["Monitores"], marker="o", label="Monitores")
plt.plot(df["Mes"], df["Teclados"], marker="o", label="Teclados")
plt.title("Ventas mensuales por producto - TecnoPlus")
plt.xlabel("Mes")
plt.ylabel("Unidades vendidas")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico de barras del total mensual
plt.figure(figsize=(12,5))
plt.bar(df["Mes"], df["Total_Mensual"])
plt.title("Ventas totales mensuales - TecnoPlus")
plt.xlabel("Mes")
plt.ylabel("Unidades totales vendidas")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# -------------------------------------------
# 7. Conclusiones
# -------------------------------------------
print("\n=== CONCLUSIONES ===")
print("1. Tendencias: Las ventas suben a mitad de año, especialmente en teclados.")
print("2. Producto más fuerte: Teclados, con las mayores unidades vendidas.")
print("3. Mes pico: {} con {} unidades totales.".format(mes_max["Mes"], mes_max["Total_Mensual"]))
