from flask import send_from_directory
from flask_frozen import Freezer
from app import app
import sys, os

freezer = Freezer(app)

@app.route('/static/images/<image>')
def images(image):
    return send_from_directory(os.path.join(app.root_path, 'static/images'), image)

@freezer.register_generator
def images():
    path = os.path.join(app.root_path, 'static/images')
    images = next(os.walk(path))[2]
    for image in images:
        yield {"image": image}

if __name__ == '__main__':
    freezer.freeze()