from flask import Flask, request, jsonify
from procesador import contar_palabras, frecuencia_palabras, resumen

app = Flask(__name__)

@app.route("/analizar", methods=["POST"])
def analizar():
    data = request.get_json()
    texto = data.get("texto", "")
    if not texto:
        return jsonify({"error": "Texto vacio"}), 400
    return jsonify({
        "palabras": contar_palabras(texto),
        "frecuencia": frecuencia_palabras(texto),
        "resumen": resumen(texto),
    })

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
