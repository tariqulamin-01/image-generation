from flask import Flask, render_template, request, send_from_directory
from diffusers import StableDiffusionPipeline
import torch
import os

app = Flask(__name__)

# Load the DreamShaper-7 model
pipe = StableDiffusionPipeline.from_pretrained("Lykon/dreamshaper-7")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Path to save generated images
IMAGE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# Ensure the image folder exists
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the prompt from the form
        prompt = request.form['prompt']

        # Generate the image
        try:
            image = pipe(prompt).images[0]

            # Save the image
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'generated_image.png')
            image.save(image_path)

            # Render the template with the generated image
            return render_template('index.html', image_path=image_path)
        except Exception as e:
            return f"Error generating image: {e}"

    # Render the template for GET requests
    return render_template('index.html')

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)