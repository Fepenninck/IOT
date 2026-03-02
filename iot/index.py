from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# estado simulado
valor_ldr = 50
potencia_led = 50


# ================================
# ROTA STATUS (simula ESP32)
# ================================
@app.route("/status")
def status():
    global valor_ldr, potencia_led

    # simula variação de luz ambiente
    variacao = random.randint(-3, 3)
    valor_ldr = max(0, min(100, valor_ldr + variacao))

    # lógica automática (ESSENCIAL DO EXERCÍCIO)
    potencia_led = 100 - valor_ldr

    return jsonify({
        "ldr": valor_ldr,
        "potencia_led": potencia_led
    })


# ================================
# MAIN
# ================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
