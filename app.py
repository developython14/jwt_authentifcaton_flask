from distutils.log import debug
from flask import Flask , render_template ,url_for
from flask import send_file, send_from_directory, safe_join, abort
import os 



app = Flask(__name__)
main_path = os.path.dirname(os.path.abspath(__file__)) 
app.config["down"] =os.path.join(main_path,'images')  


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/download')
def down():
    return send_from_directory(app.config["down"],path =app.config["down"], filename='zaki12.jpg', as_attachment=True)

if __name__ == '__main__':
    app.run( debug=True)