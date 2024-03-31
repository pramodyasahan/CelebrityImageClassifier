from flask import Flask, jsonify, request
import util

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def classify_image():
    if request.method == 'POST':
        image_data = request.form.get('image_data')
        if image_data:
            response = jsonify(util.classify_image(image_data))
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            return jsonify({'error': 'No image data provided'}), 400
    elif request.method == 'GET':
        return 'This endpoint accepts POST requests only.', 405


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(port=5000)
