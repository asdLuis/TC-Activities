#proyecto final  v.2
#preguntas y respuestas de mate
import random

correcto = 0

def mostrarRespuesta(r,rc):
    if r==rc:
        frasesWin = random.randint(1,5)
        if frasesWin == 1:
            print("Perfecto")
        elif frasesWin == 2:
            print("Excelente")
        elif frasesWin == 3:
            print("Muy bien")
        elif frasesWin == 4:
            print("Genial")
        elif frasesWin == 5:
            print("Muy bien")
        global correcto
        correcto += 1
    else:
        frasesLose = random.randint(1,5)
        if frasesLose == 1:
            print("Lastima. La respuesta era ",rc,",no", r)
        elif frasesLose == 2:
            print("Incorrecto. La respuesta era ",rc,",no", r)
        elif frasesLose == 3:
            print("Falso. La respuesta era ",rc,",no", r)
        elif frasesLose == 4:
            print("Eres una decepcion para tu familia. La respuesta era ",rc,",no", r)
        elif frasesLose == 5:
            print("Otra mal y te repruebo! La respuesta era ",rc,",no", r)

def mandarPreguntasDeMate():
    preguntasMate = [
        ["Que valor tiene el termino que falta en la suma:  16+__=30: ", 14],
        ["Cual es la raiz de 2 al cuadrado: ", 2],
        ["Tengo 20 metros de cinta roja para hacer lazos en unos paquetes de regalo idénticos. Para cada lazo necesito 50 centímetros de cinta. ¿Cuántos lazos puedo hacer? ", 40],
        ["Cuanto es 2+2? ", 4],
        ["Cual es el valor de la cotangente de 45 grados? ", 1]
        ]
    for pregunta in preguntasMate:
        i = 0
        p = pregunta[i]
        rc = pregunta[1]
        r=int(input(p))
        mostrarRespuesta(r,rc)
        i +=1
    print('Este es el final de la seccion de Matematicas, tu puntaje es', correcto, 'y recuerda seguir usando AprendeTec!')
    practica = str(input("Quieres practicar otra vez? s/n: "))
    if practica =="s":
        incio()
    else:
        print("Gracias por utilizar AprendeTec")

def mandarPreguntasDeQuimica():
    preguntasQuimica = [
        ["Es el proceso por el cual las plantas y algunos organismos usan la luz del sol para transformar el CO2 y el agua en azúcares y oxígeno  ", "fotosintesis"],
        ["¿Cuál es el animal más grande que habita la Tierra?  la ballena azul, el elefante o un ratón ", "la ballena azul"],
        ["Las aves evolucionaron a partir de los dinosaurios. ¿Verdadero o falso? ", "verdadero"],
        ["¿Qué órgano del cuerpo humano consume más energía? el cerebro, el corazon, o los pulmones ", "el cerebro"],
        ["¿Cuál es la fórmula química del agua? ", "h2o"]
        ]
    for pregunta in preguntasQuimica:
        i = 0
        p = pregunta[i]
        rc = pregunta[1]
        r=str(input(p)).lower()
        mostrarRespuesta(r,rc)
        i +=1
    print('Este es el final de la seccion de Quimica, tu puntaje es', correcto, 'y recuerda seguir usando AprendeTec!')
    practica = str(input("Quieres practicar otra vez? s/n: "))
    if practica =="s":
        incio()
    else:
        print("Gracias por utilizar AprendeTec. Vuelve pronto!")
    
#bienvenida
def incio():
    global correcto
    correcto = 0
    print("Bienvendido a AprendeTec")
    t=int(input("Quieres estudiar matemáticas o ciencias, escribe 1 para mate o 0 para ciencias: "))
    #situacion otro numero
    while t<0 or t>1 :
        t=int(input("Escribe 1 para mate o 0 para ciencias:"))

    #situacion mate
    if t==1:
        print("Esto es de Mate!")
        mandarPreguntasDeMate()
                
    #situacion ciencias
    elif t==0:
        print("Esto es de Ciencias!")
        mandarPreguntasDeQuimica()

incio()
