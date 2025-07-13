# api.py
from flask import Flask, request, jsonify
import os
from chester.run_inference import run_on_file  # à adapter selon structure réelle

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image = request.files['image']
    path = f"/tmp/{image.filename}"
    image.save(path)

    result = run_on_file(path)  # Cette fonction retourne un dict avec prédictions
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
