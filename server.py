from flask import Flask, request, jsonify

app = Flask(__name__)

# Informações do ônibus (hardcoded)
bus_info = {
    "busNumber": "1234",
    "busLine": "Linha 5 - Centro",
    "maxLotation": 50
}

# Variável para armazenar a lotação atual
current_lotation = 0

@app.route('/api/bus', methods=['GET', 'POST'])
def bus():
    global current_lotation

    if request.method == 'POST':
        data = request.get_json()

        if not data or 'resert' not in data:
            return jsonify({"error": "Invalid request body"}), 400

        # Incrementar ou decrementar lotação
        try:
            change = int(data['resert'])
        except ValueError:
            return jsonify({"error": "Invalid value for 'resert', must be an integer"}), 400

        # Atualizar a lotação atual, garantindo que não ultrapasse os limites
        new_lotation = current_lotation + change

        if new_lotation < 0 or new_lotation > bus_info["maxLotation"]:
            return jsonify({"error": "Lotation out of bounds"}), 400

        current_lotation = new_lotation
        return jsonify({"message": "Bus lotation updated successfully", "busLotation": current_lotation}), 200

    # Para método GET, retorna as informações do ônibus
    return jsonify({
        "busInfo": bus_info,
        "busLotation": current_lotation
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
