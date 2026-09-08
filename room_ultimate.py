import time
inventario = []
import matplotlib.pyplot as plt
import random
vidas = 3
pistas = 2
def mostrar_estado():
    print(f"❤️  Vidas: {vidas}   💡 Pistas: {pistas}")
    menu_principal()
def menu_principal():
    print("\n MENU PRINCIPAL")
    print("1: nueva partida")
    print("2: continuar partida")
    print("3: pedir pistas")
    print("4: salir ")
    menu=input("elige una opcion: ")
    if menu == "1":
        sobreescribir=input("si inicias una nueva partida se borraran los datos no guardados\n si ? \n :")
        if sobreescribir.lower() == "si":
            inventario.clear()
            intro()
        elif sobreescribir.lower() == "no":
             menu_principal()   
    elif menu == "2":
        habitacion()
    elif menu == "3":
        usar_pista()
    elif menu == "4":
        exit()
    else:
        print("opcion invalida")
        menu_principal()        

def usar_pista():
    global pistas
    if pistas <=  0:
        print("No te quedan pistas disponibles.")
        menu_principal()
    resp = input("¿Quieres usar una pista? (si/no): ").lower()
    if resp != "si":
        menu_principal()
    pistas -= 1
    pista=input("ingresa que necesitas saber:\n 1: caja 1 \n 2: caja 2 \n 3: triqui \n 4: pregunta final \n elige:" )
    if pista == "1":
        print("es un numero de un digito")
        mostrar_estado()
        
    elif pista == "2":
        print("entre amor, dinero y familia, piensa cuál de esas suele representarse como el vínculo o legado en historias de este tipo")    
        mostrar_estado()

    elif pista == "3":
        print("tu enemigo actua de manera aleatoria no esperes que trate de cortarte intencionadamente")
    elif pista == "4":
        print("Actualmente estamos condicionados por el entorno")
    else: 
        print("respuesta invalida")       


def perder_vida():
    global vidas
    vidas -= 1
    print(f"💔 Has perdido una vida.")
    mostrar_estado()
    
    if vidas <= 0:
        nueva_partida()
    
def mostrar_imagen():
    img = plt.imread("Saw-2004-Jigsaw-as-Billy-the-Puppet.jpg") 
    plt.imshow(img)                                               
    plt.axis("off")
    plt.show(block=False)
    plt.pause(3)
    plt.close()

def pausa():
    time.sleep(2)

def intro():
    print("Bienvenido jugador seguro sabras por que estas aqui")
    pausa()
    mostrar_imagen()
    
    print("Te despiertas en una habitación oscura, parece un hospital, al lado tienes un cadaver. La puerta está cerrada con llave.")
    pausa()
    print("Debes encontrar la forma de salir.")
    pausa()
    habitacion()

def final():
    print("Felicidades jugador haz escapado de mi habitacion," \
    "antes de que te vayas tengo una pequeña pregunta que hacerte quieres responder si o no?")
    
    eleccion=input("elige cuidadosamente:")
    if eleccion.lower() == "si":
        print("La libertad es un ﬁn en sí misma." \
        " Somos libres para elegir subjetivamente entre el bien o el mal y hacer lo que dicta nuestro corazón para ser felices")
        v=input("crees que es verdadero? escribe V si no escribe F: ")
        
        if v.lower() == "v":
            print("incorrecto")
            
            perder_vida()
            
        elif v.lower() == "f": 

            print("Correcto: eres libre de irte espero que con esta experiencia no cometas mas errores")
            print("FELICIDADES haz terminado el juego") 
            exit()
        else:
            print("respuesta invalida")       
    elif eleccion.lower() == "no":
        cont=0
        while True :
         badboy=input("Mala respuesta RESPONDE otra vez: ")
         
         if badboy == "no":
             cont +=1
             if cont == 2:
               print(" \n RESPONDE LA MALDITA PREGUNTA 😡 \n")
               img = plt.imread("jigsaw_enojado.jpeg")
               plt.imshow(img)                                               
               plt.axis("off")
                   
               plt.show(block=False)
               plt.pause(3)
               plt.close()
               if badboy == "si" :
                 return final()
                
               
             elif cont == 3: 
              perder_vida()
              
         else: 
             badboy == "si"
             final()
    else:
        print("opcion invalida")
        final()
         
    final()
    exit()
def nueva_partida():
    print("Fue un juego divertido, ADIOS\n" \
         "mueres 🪦  ☠️\n")
    otra_vez=input("perdiste, pero eso no significa que no puedas jugar otra vez"
    " JUEGAS CONMIGO OTRA VEZ? SI O NO ? Respuesta:")
    if otra_vez.lower() == "si":
        intro()
    elif otra_vez.lower() == "no":
        exit()     
    else:
        print("opcion invalida")
        nueva_partida()    
def habitacion():
    print("\n📍 Estás en la habitación principal.")
    print("Opciones:")
    print("1. Revisar la cama")
    print("2. Revisar el escritorio")
    print("3. mirar la pared")
    print("4. cadaver")
    print("5. Intentar abrir la puerta")
    print("0")
    print("6. Ver inventario")
    

    opcion = input("Elige una opción: ")

    if opcion == "1":
        cama()
    elif opcion == "2":
        escritorio()
    elif opcion == "3":
        pared()
    elif opcion == "4":
        cuerpo()    
    elif opcion == "5":
        puerta()    
    elif opcion == "6":
        print("Inventario:", inventario)
        habitacion()
    elif opcion == "0":
        final()
    else:
        print("Opción inválida.")
        habitacion()
        
def cama():
    print("\n🛏️ Revisas debajo de la cama...")
    pausa()
    print("Encuentras dos cajas que te pide una contraseña cada una")
    cajas=input("quieres inspeccionar\n la caja 1: 1 \n la caja 2: 2 \n volver a la habitacion: 3\n Elige una opcion: ")

    if cajas == "1":
          
          num=input("Una caja con un panel numerico\n"
          "RESPONDE\n"
          "un cuaderno y un lapiz cuestan 110 dolares en total. el cuaderno cuesta 100 dolares mas que el lapiz\n"
          "¿cuanto cuesta el lápiz?\n"
          "A: 5\n"
          "B: 10\n"
          "C: 15\n"
          "Elige con cuidado: ")
        
          
          if num.lower() == "a" : 
                if "****5" not in inventario:
                  print("abres la caja y encuentras un papel con lo que parece ser un numero de un codigo:\n"
                  "****5")
                  inventario.append("****5")
                  habitacion()
                elif "****5" in inventario :
                    print("no hay nada mas aqui")
                    habitacion()
          else:
                perder_vida()

    elif cajas == "2":
        print("Una caja con teclado puramente de letras\n")
        print("¿qué es lo más importante en la vida?")
        respuesta=input("incluso alguien como tu puede responder eso \n:" \
        "A: amor\n" \
        "B: dinero\n" \
        "C: familia\n")
        if respuesta.lower() == "c":
            print("haz obtenido una llave pequeña y un bisturi")
            if "llave pequeña" not in inventario:
                inventario.append("llave pequeña")
                if "bisturi" not in inventario:
                 inventario.append("bisturi")
                 habitacion()
            elif "llave pequeña" in inventario:
                print("aqui no hay nada mas") 
                habitacion()   
        else:
            perder_vida()
    else:
        habitacion()        
                    
def escritorio():
    print("\n🗄️ Revisas el escritorio...")
    pausa()
    cajon=input("El escritorio tiene dos cajones cual quieres ver\n"
    "1:cajon 1\n"
    "2:cajon 2\n"
    "volver a la habitacion: 3\n"
    "elige:")

    if cajon == "1":    
        if "llave pequeña" in inventario:
          print("Encuentras un pedazo de codigo: **32*")
          inventario.append("**32*")
          habitacion()
        else:
            print("necesito una llave para abrir este cajon\n")
            habitacion()  
    elif cajon == "2":
        print("esta medio abierto si lo fuerzo podria abrirlo ")
        print("algo te dice que no deberias ni tocarlo" )
        abrir=input("lo abres?\n si o no; \n")
        if abrir.lower() == "si":
            print("lo golpeas muy fuerte causando que algo se accione dentro de este\n" \
            "sientes un dolor en el abdomen")
            perder_vida()
        elif abrir == "no":
            print("Mejor no arriesgarme")
            habitacion()
    else:
        habitacion()

def pared():
    print("\n🧱 Miras la pared. Hay un tablero de Triqui dibujado con tiza y una vieja bocina.")

    if "67***" in inventario:
        print("El tablero ya está resuelto. No parece quedar nada más aquí.")
        habitacion()
        return

    if "5 x de madera" not in inventario:
        print("El tablero está ahí, pero no tienes con qué jugar. Necesitas fichas.")
        habitacion()
        return

    print("Una voz distorsionada sale de la bocina:")
    print("'Juega conmigo una partida de Triqui, humano. Gana, y te ganarás un pedazo del código.'")
    listo = input("¿Quieres jugar? si o no: ")

    if listo.lower() != "si":
        print("'Como quieras. Estaré aquí cuando cambies de opinión.'")
        habitacion()
        return

    resultado = jugar_triqui()

    if resultado == "gana_jugador":
        print("\n🎉 La bocina cruje: 'Interesante... aquí tienes tu recompensa.'")
        print("Un pedazo de papel cae de una ranura en la pared: 67***")
        inventario.append("67***")
        habitacion()
    elif resultado == "empate":
        print("\n'Un empate... no ganas, pero tampoco pierdes. Vuelve cuando te sientas más valiente.'")
        habitacion()
    else:
        print("\n💀 'Perdiste.'")
        perder_vida()
        


def triqui_tablero_vacio():
    """Crea la matriz 3x3 que representa el tablero de Triqui."""
    return [[" " for _ in range(3)] for _ in range(3)]


def triqui_mostrar(tablero):
    print()
    for i, fila in enumerate(tablero):
        print(f" {fila[0]} | {fila[1]} | {fila[2]} ")
        if i < 2:
            print("---+---+---")
    print()


def triqui_posiciones_disponibles(tablero):
    return [(f, c) for f in range(3) for c in range(3) if tablero[f][c] == " "]


def triqui_hay_ganador(tablero, ficha):
    for fila in tablero:
        if all(celda == ficha for celda in fila):
            return True
    for col in range(3):
        if all(tablero[fila][col] == ficha for fila in range(3)):
            return True
    if all(tablero[i][i] == ficha for i in range(3)):
        return True
    if all(tablero[i][2 - i] == ficha for i in range(3)):
        return True
    return False


def triqui_turno_jugador(tablero):
    """Pide al jugador una posición válida usando sus '5 X de madera'."""
    while True:
        try:
            entrada = input("Coloca tu ficha (fila columna, 0-2 0-2): ")
            fila, columna = map(int, entrada.strip().split())
            if fila not in range(3) or columna not in range(3):
                print("Posición fuera del tablero, intenta de nuevo.")
                continue
            if tablero[fila][columna] != " ":
                print("Esa casilla ya está ocupada.")
                continue
            tablero[fila][columna] = "X"
            return
        except ValueError:
            print("Formato inválido, escribe dos números separados por un espacio, ej: 1 2")


def triqui_turno_maquina(tablero):
    """Jigsaw (la máquina) elige aleatoriamente una posición disponible."""
    disponibles = triqui_posiciones_disponibles(tablero)
    fila, columna = random.choice(disponibles)
    tablero[fila][columna] = "O"
    print(f"Jigsaw coloca su ficha en ({fila}, {columna}).")


def jugar_triqui():
    """
    Juega una partida de Triqui contra la máquina.
    Devuelve "gana_jugador", "gana_maquina" o "empate".
    """
    tablero = triqui_tablero_vacio()
    turno = "jugador"  # el jugador (X) empieza

    triqui_mostrar(tablero)

    while True:
        if turno == "jugador":
            triqui_turno_jugador(tablero)
            ficha_actual = "X"
        else:
            triqui_turno_maquina(tablero)
            ficha_actual = "O"

        triqui_mostrar(tablero)

        if triqui_hay_ganador(tablero, ficha_actual):
            return "gana_jugador" if turno == "jugador" else "gana_maquina"

        if not triqui_posiciones_disponibles(tablero):
            return "empate"

        turno = "maquina" if turno == "jugador" else "jugador"


def cuerpo():
    if "bisturi" in inventario:
        if "5 x de madera" not in inventario:
            print("Abriste su brazo y encuentras 5 X de madera, ¿para qué servirán?")
            inventario.append("5 x de madera")
        else:
            print("Ya revisaste el cuerpo, no queda nada más aquí.")
        habitacion()
    else:
        print("en su brazo derecho escrito con marcador dice cortame"
        "necesito algo para cortar ")
        habitacion()
def puerta():
    print("\n🚪 La puerta tiene un panel numérico.")
    if "67***" in inventario:
        codigo = input("Ingresa el código: ")
        if codigo == "67325":
            print("🔓 El panel se desbloquea...")
            pausa()
            print("🎉 ¡Has escapado del cuarto!")
            final()
            
        else:
            print("Código incorrecto.")
            habitacion()
    else:
        print("No sabes el código.")
        
    habitacion()
    
menu_principal()