def tragaperras(monedas):
    # Símbolos que puede tener cada rueda
    simbolos = ["🍇", "🍒", "🍋", "🔔", "7️⃣", "BAR"]
    
    # Preguntar al jugador cuánto quiere apostar
    while True:
        try:
            apuesta = int(input("¿Cuántas monedas quieres apostar? "))
            if apuesta > monedas or apuesta <= 0:
                print(f"No puedes apostar eso. Tienes {monedas} monedas.")
            else:
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Gira las tres ruedas
    rueda1 = random.choice(simbolos)
    rueda2 = random.choice(simbolos)
    rueda3 = random.choice(simbolos)
    
    # Muestra los resultados
    print(f"Resultado: {rueda1} | {rueda2} | {rueda3}")
    
    # Comprueba si hay algún premio
    if rueda1 == rueda2 == rueda3:
        if rueda1 == "7️⃣":
            ganancia = apuesta * 10
            print(f"¡Jackpot! Has ganado {ganancia} monedas.")
            monedas += ganancia
        else:
            ganancia = apuesta * 2
            print(f"¡Has ganado {ganancia} monedas con {rueda1}!")
            monedas += ganancia
    else:
        monedas -= apuesta
        print(f"Lo siento, no has ganado esta vez. Te quedan {monedas} monedas.")

    return monedas

# Inicializar las monedas del jugador
monedas_iniciales = 50
print(f"Empiezas con {monedas_iniciales} monedas.")

# Jugar hasta que el jugador se quede sin monedas o decida parar
while monedas_iniciales > 0:
    monedas_iniciales = tragaperras(monedas_iniciales)
    if monedas_iniciales <= 0:
        print("Te has quedado sin monedas. ¡Gracias por jugar!")
        break
    continuar = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if continuar != 's':
        print(f"Has terminado con {monedas_iniciales} monedas. ¡Gracias por jugar!")
        break