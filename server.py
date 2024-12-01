from flask import Flask, request, jsonify

app = Flask(__name__)

bus_info = {
    "busNumber": "1234",
    "busLine": "Linha 5 - Centro",
    "maxLotation": 50
}

current_lotation = 0

def determine_status(lotation):
    if lotation == 0:
        return "Vazio"
    elif lotation < bus_info["maxLotation"]:
        return "Normal"
    else:
        return "Lotado"

@app.route('/api/bus', methods=['GET', 'POST'])
def bus():
    global current_lotation

    if request.method == 'POST':
        data = request.get_json()

        if not data or 'resert' not in data:
            return jsonify({"error": "Invalid request body"}), 400

        try:
            change = int(data['resert'])
        except ValueError:
            return jsonify({"error": "Invalid value for 'resert', must be an integer"}), 400

        new_lotation = current_lotation + change
        if new_lotation < 0 or new_lotation > bus_info["maxLotation"]:
            return jsonify({"error": "Lotation out of bounds"}), 400

        current_lotation = new_lotation
        status = determine_status(current_lotation)

        return jsonify({
            "message": "Bus lotation updated successfully",
            "busLotation": current_lotation,
            "status": status
        }), 200

    status = determine_status(current_lotation)
    return jsonify({
        "busInfo": bus_info,
        "busLotation": current_lotation,
        "status": status
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
