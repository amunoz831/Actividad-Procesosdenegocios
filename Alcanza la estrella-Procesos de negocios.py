import random
#Se utiliza random para generar el atributo random de las preguntas y el atributo del dado.

def generar_preguntas():
    preguntas= [
        ("¿Cuál es la capital de Francia?", "A) Madrid", "B) París", "C) Roma", "B"),
        ("¿Cuál es el símbolo químico del oxígeno?", "A) O", "B) Ox", "C) Oxg", "A"),
        ("¿En qué año comenzó la Segunda Guerra Mundial?", "A) 1939", "B) 1945", "C) 1914", "A"),
        ("¿Cuál es el río más largo del mundo?", "A) Amazonas", "B) Nilo", "C) Yangtsé", "B"),
        ("¿Cuál es la capital de Australia?", "A) Sídney", "B) Melbourne", "C) Canberra", "C"),
        ("¿Quién escribió la novela '1984'?", "A) George Orwell", "B) Aldous Huxley", "C) Ray Bradbury", "A"),
        ("¿En qué continente se encuentra Egipto?", "A) África", "B) Asia", "C) Europa", "A"),
        ("¿Cuál es el metal más ligero?", "A) Aluminio", "B) Titanio", "C) Litio", "C"),
        ("¿Quién pintó 'La última cena'?", "A) Vincent van Gogh", "B) Leonardo da Vinci", "C) Pablo Picasso", "B"),
        ("¿Cuál es la montaña más alta de América?", "A) Monte McKinley", "B) Aconcagua", "C) Monte Rainier", "A"),
        ("¿Cuál es la moneda oficial de Japón?", "A) Yuan", "B) Rupia", "C) Yen", "C"),
        ("¿En qué año ocurrió el primer alunizaje?", "A) 1969", "B) 1972", "C) 1955", "A"),
        ("¿Qué elemento químico tiene el símbolo 'Fe'?", "A) Fluoruro", "B) Hierro", "C) Mercurio", "B"),
        ("¿En qué año se firmó la Declaración de Independencia de Estados Unidos?", "A) 1776", "B) 1789", "C) 1804", "A"),
        ("¿Quién pintó 'La noche estrellada'?", "A) Claude Monet", "B) Vincent van Gogh", "C) Salvador Dalí", "B"),
        ("¿Cuál es el océano más grande?", "A) Océano Atlántico", "B) Océano Índico", "C) Océano Pacífico", "C"),
        ("¿Qué famoso científico desarrolló la teoría de la relatividad?", "A) Isaac Newton", "B) Albert Einstein", "C) Galileo Galilei", "B"),
        ("¿Cuál es el planeta más grande del sistema solar?", "A) Júpiter", "B) Saturno", "C) Neptuno", "A"),
        ("¿Qué famoso artista es conocido por su estilo de 'arte pop'?", "A) Pablo Picasso", "B) Andy Warhol", "C) Jackson Pollock", "B"),
        ("¿En qué país se encuentra la Gran Muralla China?", "A) Japón", "B) China", "C) Corea del Sur", "B"),
        ("¿Quién escribió la obra 'Romeo y Julieta'?", "A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "A"),
        ("¿Cuál es el metal más precioso?", "A) Plata", "B) Oro", "C) Platino", "B"),
        ("¿En qué año comenzó la Primera Guerra Mundial?", "A) 1914", "B) 1918", "C) 1922", "A"),
        ("¿Cuál es el país más grande del mundo en términos de área terrestre?", "A) China", "B) Rusia", "C) Estados Unidos", "B"),
        ("¿Quién escribió 'Cien años de soledad'?", "A) Julio Cortázar", "B) Gabriel García Márquez", "C) Pablo Neruda", "B"),
        ("¿Cuál es el hueso más largo del cuerpo humano?", "A) Fémur", "B) Tibia", "C) Húmero", "A"),
        ("¿En qué continente se encuentra el desierto del Sahara?", "A) Asia", "B) África", "C) América", "B"),
        ("¿Quién fue el primer presidente de Estados Unidos?", "A) Thomas Jefferson", "B) Abraham Lincoln", "C) George Washington", "C"),
        ("¿Cuál es la moneda oficial de Reino Unido?", "A) Dólar", "B) Euro", "C) Libra esterlina", "C"),
        ("¿En qué año cayó el Muro de Berlín?", "A) 1989", "B) 1991", "C) 1987", "A"),
        ("¿Cuál es el elemento más abundante en la corteza terrestre?", "A) Silicio", "B) Oxígeno", "C) Hierro", "B"),
        ("¿En qué país se encuentra la Torre Eiffel?", "A) España", "B) Francia", "C) Italia", "B"),
        ("¿Qué famoso científico formuló las leyes del movimiento?", "A) Isaac Newton", "B) Albert Einstein", "C) Galileo Galilei", "A"),
        ("¿Cuál es el animal terrestre más grande del mundo?", "A) Elefante africano", "B) Ballena azul", "C) Jirafa", "B"),
        ("¿En qué año se fundó la Ciudad del Vaticano?", "A) 1929", "B) 1945", "C) 1956", "A"),
        ("¿Cuál es el río más largo de América del Norte?", "A) Río Colorado", "B) Río Mississippi", "C) Río Amazonas", "B"),
        # Aca podemos agregar mas preguntas para hacer del juego mas interesante
    ]
    return preguntas
    
def aplicar_castigo():
    # Teniendo en cuenta que estamos en una matriz, jugamos con las posiciones para ejecutar los catigos
    castigos = [
        ("Puente", 3),
        ("Resbalo", 2),
        ("Calavera", -1),  # Con esto determinamos que el jugador vuelve al inicio
    ]
    castigo, retroceso = random.choice(castigos)
    return castigo, retroceso #Aca decidimos que castigo se otorga y se muestra al jugador que castigo se le impondra

def jugar():
    #Se inicializa el juego con los jugadores en la posicion 1
    jugadores = [{"posicion": 1, "aciertos": 0}, {"posicion": 1, "aciertos": 0}]
    
    while True:
        preguntas = generar_preguntas()
        random.shuffle(preguntas)
        #Se determinan los turnos y se genera todo el codigo para tirar los dados y ver la situacion de las preguntas
        
        for jugador_idx in range(2):
            jugador = jugadores[jugador_idx]
            print(f"Turno del jugador {jugador_idx + 1}")
            
            input("Presiona Enter para lanzar el dado...")
            dado = random.randint(1, 6)
            print(f"El jugador sacó un {dado}")
            
            nueva_posicion = jugador["posicion"] + dado
            if nueva_posicion > 20:
                nueva_posicion = 20
                
            pregunta, opcion_a, opcion_b, opcion_c, respuesta_correcta = preguntas.pop()
            print(pregunta)
            print(opcion_a)
            print(opcion_b)
            print(opcion_c)
            
            respuesta = input("Elige la opción correcta (A/B/C): ").upper()
            
            if respuesta == respuesta_correcta:
                print("Respuesta correcta. Permaneces en la casilla.")
                jugador["aciertos"] += 1
            else:
                print("Respuesta incorrecta. ¡Castigo!")
                castigo, retroceso = aplicar_castigo()
                print(f"Se te aplica el castigo: {castigo}")
                nueva_posicion -= retroceso
                if nueva_posicion < 1:
                    nueva_posicion = 1
            
            jugador["posicion"] = nueva_posicion
            
            print(f"Jugador {jugador_idx + 1} está en la casilla {jugador['posicion']} con {jugador['aciertos']} aciertos.")
            
            if jugador["posicion"] == 20:
                print(f"¡El jugador {jugador_idx + 1} ha ganado!")
                return
            
            print("Posiciones actuales:")
            for idx, j in enumerate(jugadores, start=1):
                print(f"Jugador {idx}: Posición {j['posicion']}, Aciertos {j['aciertos']}")
            print("-" * 20)

jugar()
