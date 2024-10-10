# Importa las librerías necesarias de Flask, CORS y RPi.GPIO
from flask import Flask, request, jsonify 
from flask_cors import CORS
import RPi.GPIO as GPIO
import time

# Inicializa la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir que otros dominios accedan a la API

# Configura el modo de pines GPIO en modo BOARD (numeración física de pines)
GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False) # Desactiva advertencias de los pines GPIO (opcional)

# Define los pines a usar
LDR_NOCHE = 24  # Pin del sensor LDR para detectar luz/no luz
LED = 22  # Pin para controlar el LED (luz exterior)

# Configuración inicial de los pines GPIO
def setUp():     
    # Configura el pin LDR_NOCHE como entrada y el pin LED como salida
    GPIO.setup(LDR_NOCHE, GPIO.IN)
    GPIO.setup(LED, GPIO.OUT)

# Configuración para solo el pin LED
def setUpLED():     
    # Configura el pin LED como salida
    GPIO.setup(LED, GPIO.OUT)

# Enciende el LED
def turnOnLed():
    print("Luz exterior encendida")  # Imprime el estado en la consola
    GPIO.output(LED, GPIO.HIGH)  # Establece el pin del LED a alto (enciende)

# Apaga el LED
def turnOffLed():
    print("Luz exterior apagada")  # Imprime el estado en la consola
    GPIO.output(LED, GPIO.LOW)  # Establece el pin del LED a bajo (apaga)

# Función para detectar si es de noche o día usando el sensor LDR
def isnight():
    # GPIO.setup(LDR_NOCHE, GPIO.IN)  # (opcional, ya configurado en setUp)
    time.sleep(0.1)  # Pausa breve para estabilidad
    ldr_value2 = GPIO.input(LDR_NOCHE)  # Lee el valor del sensor LDR
    if ldr_value2 == 0:  # Si el valor es 0, es de día
        ldr_value2 = "dia"
    else:  # Si el valor es distinto, es de noche
        ldr_value2 = "noche"
    return ldr_value2  # Devuelve "dia" o "noche"

# Limpia los pines GPIO (libera los recursos)
def limpiar():
    GPIO.cleanup()

# Ruta de la API para limpiar los pines GPIO
@app.route('/limpiarpines', methods=['GET'])
def limpiarpines():
    limpiar()  # Llama a la función para limpiar los pines
    return jsonify({"status": "pines limpios"}), 200  # Devuelve una respuesta JSON

# Ruta de la API para controlar el encendido y apagado de la luz exterior (LED)
@app.route("/luzexterior",methods=['POST'])
def onOffLuz():
    try:
        setUpLED()  # Configura el pin del LED
        data = request.json  # Obtiene los datos JSON del cuerpo de la petición
        accion = data.get("led")  # Extrae el valor "led" de los datos
        if accion == 0:  # Si el valor es 0, apaga el LED
            turnOffLed()
            return jsonify({"estado": "luz apagada"})  # Respuesta JSON indicando que está apagado
        else:  # Si el valor es distinto de 0, enciende el LED
            turnOnLed()
            return jsonify({"estado": "luz encendida"})  # Respuesta JSON indicando que está encendido
    except:
        limpiar()  # En caso de error, limpia los pines
        return jsonify({"message": "Ha ocurrido un error al encender o apagar la luz"})  # Error en JSON

# Ruta de la API para activar el circuito de detección de luz (día/noche)
@app.route('/activarcircuito', methods=['POST'])
def activarCircuito():
    try:
        setUp()  # Configura los pines de entrada/salida
        data = request.json  # Obtiene los datos JSON del cuerpo de la petición
        accion = data.get("circuito")  # Extrae el valor "circuito" de los datos
        bucle = True
        if accion == 1:  # Si el valor es 1, inicia el bucle
            bucle = True
        else:  # Si el valor es distinto de 1, detiene el bucle
            bucle = False
        while bucle:
            # Lee el valor del sensor LDR para determinar si es de día o de noche
            ldr_val2 = isnight()
            if ldr_val2 == "dia":  # Si es de día, apaga el LED
                turnOffLed()
            else:  # Si es de noche, enciende el LED
                turnOnLed()
            time.sleep(5)  # Espera 5 segundos antes de leer nuevamente
            limpiar()  # Limpia los pines después de cada ciclo
        return jsonify({"message": "activación de circuito finalizada"})  # Respuesta cuando termina el bucle
    except KeyboardInterrupt:  # Captura una interrupción manual (Ctrl+C)
        limpiar()  # Limpia los pines
        return jsonify({"message": "Error: PINES LIMPIOS"})  # Mensaje de error en JSON
    finally:
        limpiar()  # Asegura que los pines se limpien al final
        return jsonify({"message": "PINES LIMPIOS"})  # Respuesta final en JSON

# Arranca la aplicación Flask
if __name__ == '_main_':  # Comprueba si el script se está ejecutando directamente
    try:
        app.run()  # Inicia el servidor Flask
        app.debug = True  # Activa el modo de depuración

        # Ejecuta la aplicación en modo producción, accesible desde otras máquinas
        #app.run(host='0.0.0.0', port=80)  # Cambia el puerto a 80 (o el que prefieras)
    except KeyboardInterrupt:  # Captura una interrupción manual (Ctrl+C)
        limpiar()  # Limpia los pines antes de salir
    finally:
        limpiar()  # Asegura la limpieza final de los pines
