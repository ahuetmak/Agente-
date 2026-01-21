from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/run', methods=['POST'])
def run_agent():
    data = request.get_json()
    response = {
        "status": "ok",
        "input": data,
        "message": "Agente invisible ejecutado correctamente."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
