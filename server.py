
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['firmware']
    path = os.path.join(UPLOAD_FOLDER, f.filename)
    f.save(path)
    return jsonify({'status': 'uploaded', 'path': path})

@app.route('/deploy', methods=['POST'])
def deploy_firmware():
    # Simulate OTA deployment (placeholder)
    filename = request.json.get('filename')
    return jsonify({'status': 'deployed', 'filename': filename})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
