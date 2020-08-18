# Simulaciones usando Python

En este taller vamos a poner a prueba tus habilidades de programación orientada a objetos. A continuación tienes 3 retos de simulación que puedes resolver con OOP, debes escoger y resolver 2.


1. **Juego de dados secretos:**
    - Existen N jugadores, cada uno con 5 dados de 6 lados.
    - Cada jugador revuelve sus dados y los tira, cada uno puede ver su propio resultado pero no el de los demás.
    - Es el turno de un jugador, este debe debe decir cuántos dados con qué número hay en la mesa y retar a otro jugador.
    - El jugador retado debe decir si lo que dice el jugador anterior es falso o si puede ser verdadero e incluso un puede haber un número superior de dados del mismo valor.
    - Su código debe simular este escenario y calcular la probabilidad de que el jugador retante esté diciendo algo falso. Debe realizar una función que reciba una estimación y calcule la probabilidad de falso.
2. **Recorrer un tablero de parqués:**
    - Es un juego de parqués con solo N jugadores, cada jugador tiene M fichas.
    - La salida de la cárcel es automática.
    - ¿Cuántos turnos se demora en terminar el juego?
3. **Gana el jugador de la carta más grande:**
    - Hay 2 jugadores.
    - Cada uno tiene un [juego stándar de 52 cartas](https://en.wikipedia.org/wiki/Standard_52-card_deck).
    - En cada turno, ambos jugadores muestran una carta.
    - El ganador del turno es quien tenga la carta más grande y se lleva la carta del otro jugador.
    - Si hay empates, se sacan cartas de nuevo hasta desempatar, el ganador del desempate se lleva todas las cartas lanzadas hasta el momento.
    - El juego se acaba cuando un jugador se queda con las 104 cartas.
    - ¿Cuántos turnos tarda en terminar el juego?

Acá, el nivel de detalle es un poco abierto, como sucedería en la vida real. Puedes hacer las suposiciones que consideres necesarias y simplificar el problema cuando como consideres necesario dentro de las restricciones dadas.

No es válido resolver el problema por medios analíticos, todo se debe hacer por medio de simulación.
