# Importa las librerías necesarias de Flask, CORS y RPi.GPIO
from flask import Flask, request, jsonify 
from flask_cors import CORS
import time

# Inicializa la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir que otros dominios accedan a la API


# Enciende el LED
def turnOnLed():
    print("Luz exterior encendida")  # Imprime el estado en la consola

# Apaga el LED
def turnOffLed():
    print("Luz exterior apagada")  # Imprime el estado en la consola

# Función para detectar si es de noche o día usando el sensor LDR
def isnight():
    # GPIO.setup(LDR_NOCHE, GPIO.IN)  # (opcional, ya configurado en setUp)
    time.sleep(0.1)  # Pausa breve para estabilidad
    ldr_value2 = 1
    if ldr_value2 == 0:  # Si el valor es 0, es de día
        ldr_value2 = "dia"
    else:  # Si el valor es distinto, es de noche
        ldr_value2 = "noche"
    return ldr_value2  # Devuelve "dia" o "noche"


# Ruta de la API para controlar el encendido y apagado de la luz exterior (LED)
@app.route("/luzexterior",methods=['POST'])
def onOffLuz():
    try:
        data = request.json  # Obtiene los datos JSON del cuerpo de la petición
        accion = data.get("led")  # Extrae el valor "led" de los datos
        if accion == 0:  # Si el valor es 0, apaga el LED
            turnOffLed()
            return jsonify({"estado": "luz apagada"})  # Respuesta JSON indicando que está apagado
        else:  # Si el valor es distinto de 0, enciende el LED
            turnOnLed()
            return jsonify({"estado": "luz encendida"})  # Respuesta JSON indicando que está encendido
    except:
        return jsonify({"message": "Ha ocurrido un error al encender o apagar la luz"})  # Error en JSON

# Ruta de la API para activar el circuito de detección de luz (día/noche)
@app.route('/activarcircuito', methods=['POST'])
def activarCircuito():
    try:
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
        return jsonify({"message": "activación de circuito finalizada"})  # Respuesta cuando termina el bucle
    except KeyboardInterrupt:  # Captura una interrupción manual (Ctrl+C)
        return jsonify({"message": "Error: PINES LIMPIOS"})  # Mensaje de error en JSON
    finally:
        return jsonify({"message": "PINES LIMPIOS"})  # Respuesta final en JSON

# Arranca la aplicación Flask
if __name__ == '_main_':  # Comprueba si el script se está ejecutando directamente
    app.run()  # Inicia el servidor Flask
    app.debug = True  # Activa el modo de depuración

    # Ejecuta la aplicación en modo producción, accesible desde otras máquinas
    #app.run(host='0.0.0.0', port=80)  # Cambia el puerto a 80 (o el que prefieras)