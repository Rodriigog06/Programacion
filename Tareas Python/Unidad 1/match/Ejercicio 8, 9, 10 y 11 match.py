import random

def jugar():
    victorias_humano = 0
    victorias_maquina = 0

    while victorias_humano < 2 and victorias_maquina < 3:
        eleccion_humano = input("Elige Piedra, Papel o Tijera: ").upper()
        
        if eleccion_humano not in ["PIEDRA", "PAPEL", "TIJERA"]:
            print("Elección no válida. Intenta de nuevo.")
            continue

        apuesta_maquina = random.randint(0, 2)
        if apuesta_maquina == 0:
            eleccion_maquina = "PIEDRA"
        elif apuesta_maquina == 1:
            eleccion_maquina = "PAPEL"
        else:
            eleccion_maquina = "TIJERA"

        print(f"La máquina ha elegido: {eleccion_maquina}")
        if eleccion_humano == eleccion_maquina:
            print("¡Es un empate!")
        elif (eleccion_humano == "PIEDRA" and eleccion_maquina == "TIJERA") or \
             (eleccion_humano == "PAPEL" and eleccion_maquina == "PIEDRA") or \
             (eleccion_humano == "TIJERA" and eleccion_maquina == "PAPEL"):
            print("¡Ganaste esta ronda!")
            victorias_humano += 1
        else:
            print("La máquina gana esta ronda.")
            victorias_maquina += 1
        print(f"Puntuación: Jugador {victorias_humano} - Máquina {victorias_maquina}\n")

    if victorias_humano == 2 or 3:
        print("¡Felicidades! Has ganado el juego.")
    elif victorias_maquina == 2 or 3 :
        print("La máquina ha ganado el juego. ¡Mejor suerte la próxima vez!")
if __name__ =="__main__" :
    jugar()
