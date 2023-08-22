from flask import Flask, render_template, send_from_directory
from flask_frozen import Freezer
from flask_flatpages import FlatPages
import sys, os

app = Flask(__name__)
freezer = Freezer(app)
pages = FlatPages(app)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/static/images/<image>')
def images(image):
    return send_from_directory(os.path.join(app.root_path, 'static/images'), image)

@freezer.register_generator
def images():
    path = os.path.join(app.root_path, 'static/images')
    images = next(os.walk(path))[2]
    for image in images:
        yield {"image": image}
 
if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		app.run(host='0.0.0.0', port=81)
