from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

TEXT_TO_IMAGE_API = "http://172.16.20.12:5001/generate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    prompt = request.form.get("prompt")  # Get from FormData

    if not prompt:
        return "Error: Prompt is required", 400

    try:
        response = requests.post(TEXT_TO_IMAGE_API, json={"prompt": prompt})
        data = response.json()

        if "image_url" in data:
            return data["image_url"]  # Return URL to display in frontend
        else:
            return "Failed to generate image", 500
    except requests.exceptions.RequestException as e:
        return f"Error connecting to API: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
