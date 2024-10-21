from flask import Flask, request, jsonify
from generate_music import generate_music
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    data = request.json
    mood = data.get('mood')

    if not mood:
        return jsonify({'error': 'Mood parameter is missing'}), 400

    try:
        audio_file = generate_music(mood)
        return jsonify({'message': 'Music generated', 'file': audio_file}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
