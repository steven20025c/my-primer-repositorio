# ==========================================
# 1. Calculadora de IVA
# ==========================================
precio = 150.50
iva = 21

monto_iva = precio * iva / 100
total = precio + monto_iva

print("Precio:", precio)
print("IVA:", monto_iva)
print("Total:", total)


# ==========================================
# 2. Conversor de Edad a Días
# ==========================================
nombre = "Carlos"
edad = 20

dias = edad * 365

print(f"Hola {nombre}, has vivido aproximadamente {dias} días.")


# ==========================================
# 3. Intercambio de Valores
# ==========================================
a = 5
b = 10

print("Antes:", a, b)

a, b = b, a

print("Después:", a, b)


# ==========================================
# 4. Formateador de Direcciones
# ==========================================
calle = "Av. Duarte"
numero = 25
ciudad = "Santo Domingo"
codigo = "10101"

print(f"{calle}, #{numero}\n{ciudad}\nCP: {codigo}")


# ==========================================
# 5. Promedio Simple
# ==========================================
nota1 = 90
nota2 = 85
nota3 = 95

promedio = (nota1 + nota2 + nota3) / 3

print(round(promedio, 2))


# ==========================================
# 6. Control de Acceso por Edad
# ==========================================
edad = 30

if edad < 18:
    print("Acceso denegado")
elif edad <= 65:
    print("Acceso permitido")
else:
    print("Acceso preferencial para adultos mayores")


# ==========================================
# 7. Clasificador de Números
# ==========================================
numero = -5

if numero > 0:
    if numero % 2 == 0:
        print("Positivo y Par")
    else:
        print("Positivo e Impar")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")


# ==========================================
# 8. Simulador de Semáforo
# ==========================================
color_semaforo = "Verde"

if color_semaforo == "Verde":
    print("Avanzar")
elif color_semaforo == "Amarillo":
    print("Frenar con precaución")
elif color_semaforo == "Rojo":
    print("Detenerse")
else:
    print("Semáforo averiado")


# ==========================================
# 9. Descuento por Compra
# ==========================================
compra = 120

if compra > 100:
    compra *= 0.85

print("Total:", compra)


# ==========================================
# 10. Año Bisiesto
# ==========================================
anio = 2024

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")


# ==========================================
# 11. Calculadora con match-case
# ==========================================
num1 = 10
num2 = 5
operador = "+"

match operador:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Operador inválido")


# ==========================================
# 12. Día de la Semana
# ==========================================
dia = 3

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número inválido")


# ==========================================
# 13. Conversor de Temperatura
# ==========================================
celsius = 30
escala = "F"

match escala:
    case "F":
        print((celsius * 9/5) + 32)
    case "K":
        print(celsius + 273.15)
    case "C":
        print(celsius)
    case _:
        print("Escala inválida")


# ==========================================
# 14. Tipo de Archivo
# ==========================================
extension = "pdf"

match extension:
    case "jpg" | "png":
        print("Imagen")
    case "mp3":
        print("Audio")
    case "pdf" | "docx":
        print("Documento de texto")
    case _:
        print("Desconocido")


# ==========================================
# 15. Conversor de Calificaciones
# ==========================================
nota = 4

match nota:
    case 1 | 2:
        print("Insuficiente")
    case 3:
        print("Suficiente")
    case 4:
        print("Notable")
    case 5:
        print("Sobresaliente")
    case _:
        print("Nota no válida")


# ==========================================
# 16. Saludo Personalizado
# ==========================================
def saludar_usuario(nombre, hora_dia):
    if hora_dia == "mañana":
        return f"¡Buenos días, {nombre}!"
    elif hora_dia == "tarde":
        return f"¡Buenas tardes, {nombre}!"
    else:
        return f"¡Buenas noches, {nombre}!"

print(saludar_usuario("Carlos", "mañana"))


# ==========================================
# 17. Conversión USD a EUR
# ==========================================
def convertir_usd_a_eur(cantidad_usd, tasa):
    return cantidad_usd * tasa

print(convertir_usd_a_eur(100, 0.92))


# ==========================================
# 18. Área de Triángulo
# ==========================================
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

print(calcular_area_triangulo(10, 8))


# ==========================================
# 19. Mayor de Tres Números
# ==========================================
def mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(mayor(5, 9, 3))


# ==========================================
# 20. Validar Contraseña
# ==========================================
def validar_longitud_password(password):
    return len(password) >= 8

print(validar_longitud_password("Python123"))


# ==========================================
# 21. Sistema Escolar
# ==========================================
def clasificar_nota(nota):
    if nota < 60:
        return "Reprobado"
    elif nota < 90:
        return "Aprobado"
    else:
        return "Excelente"

print(clasificar_nota(95))


# ==========================================
# 22. IMC
# ==========================================
def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)

    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    else:
        return "Sobrepeso"

print(calcular_imc(70, 1.75))


# ==========================================
# 23. Validador de Triángulos
# ==========================================
def tipo_triangulo(a, b, c):
    if a+b <= c or a+c <= b or b+c <= a:
        return "No forma un triángulo"

    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

print(tipo_triangulo(5,5,5))


# ==========================================
# 24. Estacionamiento
# ==========================================
def costo_estacionamiento(horas):
    if horas <= 2:
        return horas * 2
    else:
        return 4 + (horas-2)*1.5

print(costo_estacionamiento(5))


# ==========================================
# 25. Cajero Automático
# ==========================================
saldo_cuenta = 500

def retirar_dinero(monto):
    global saldo_cuenta

    if monto > saldo_cuenta:
        print("Saldo insuficiente")
    elif monto % 10 != 0:
        print("Debe retirar múltiplos de 10")
    else:
        saldo_cuenta -= monto
        print("Nuevo saldo:", saldo_cuenta)

retirar_dinero(100)


# ==========================================
# 26. Número Primo
# ==========================================
def es_primo(numero):
    match numero:
        case 2 | 3 | 5 | 7:
            return "Primo"
        case 1 | 4 | 6 | 8 | 9 | 10:
            return "Compuesto"
        case _:
            return "Fuera del rango"

print(es_primo(7))


# ==========================================
# 27. Tarifas de Envío
# ==========================================
def calcular_envio(peso, zona):
    match zona:
        case "Norte":
            tarifa = 5
        case "Sur":
            tarifa = 4
        case "Centro":
            tarifa = 3
        case _:
            return "Zona inválida"

    return peso * tarifa

print(calcular_envio(8, "Sur"))


# ==========================================
# 28. Piedra, Papel o Tijera
# ==========================================
jugador1 = "Piedra"
jugador2 = "Tijera"

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "Piedra" and jugador2 == "Tijera") or \
     (jugador1 == "Papel" and jugador2 == "Piedra") or \
     (jugador1 == "Tijera" and jugador2 == "Papel"):
    print("Gana Jugador 1")
else:
    print("Gana Jugador 2")


# ==========================================
# 29. Impuesto Progresivo
# ==========================================
def salario_neto(salario):
    if salario < 1500:
        impuesto = 0
    elif salario <= 3000:
        impuesto = (salario-1500)*0.10
    else:
        impuesto = (1500*0.10)+(salario-3000)*0.20

    return salario-impuesto

print(salario_neto(4000))


# ==========================================
# 30. Bono por Desempeño
# ==========================================
ventas_mes = 60
asistencia_perfecta = True

if ventas_mes > 50 and asistencia_perfecta:
    print("Bono Premium")
elif ventas_mes > 50 or asistencia_perfecta:
    print("Bono Estándar")
else:
    print("Sin bono")