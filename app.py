from distutils.log import debug
from flask import Flask , render_template
from flask import send_file, send_from_directory, safe_join, abort
import os 



app = Flask(__name__)
app.config["down"]  = os.path.abspath(os.getcwd())


@app.route("/")
def hello_world():
    return render_template('index.html')

app.route('/download')
def down():
    return app.config["down"]

if __name__ == '__main__':
    app.run( debug=True)