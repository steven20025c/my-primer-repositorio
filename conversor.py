
segs_totales = int(input("Introduce la cantidad de segundos: "))

# El operador // hace la división entera
minutos = segs_totales / 60

# El operador % obtiene el residuo (lo que sobra)
segundos_restantes = segs_totales % 60

print(f"Resultado: {minutos} minutos con {segundos_restantes} segundos.")

