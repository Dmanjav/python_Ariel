from dagor import JuegoD10, JugadorD10Interactivo, JugadorD10Aleatorio, JugadorD10Estrategico

j1 = JugadorD10Aleatorio("Aleatorio")
j2 = JugadorD10Estrategico("Estratégico")

juego = JuegoD10(j1, j2)

juego.inicia(veces=1000)