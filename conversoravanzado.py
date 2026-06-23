# 1. Entrada: Convertimos a entero para evitar decimales desde el inicio
segs_totales = int(input("Introduce la cantidad de segundos (pueden ser negativos): "))

# 2. Proceso:
# Usamos el valor absoluto para calcular cantidades reales
segs_abs = abs(segs_totales)

# // es la división entera (ignora los decimales)
mins = segs_abs // 60

# % es el residuo (lo que sobra después de quitar los minutos)
segs_restantes = segs_abs % 60

# Determinamos el signo para la salida
signo = "-" if segs_totales < 0 else ""

# 3. Salida
print(f"Equivale a: {signo}{mins} minutos y {segs_restantes} segundos.")