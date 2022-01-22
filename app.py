from distutils.log import debug
from flask import Flask, jsonify , render_template, request ,url_for
from flask import send_file, send_from_directory, safe_join, abort
import os 
from flask.views import MethodView




app = Flask(__name__)
main_path = os.path.dirname(os.path.abspath(__file__)) 
app.config["down"] =os.path.join(main_path,'images')  




class toma(MethodView) : 
    def get(self):
        return 'mustapha belkassem'
    def post (self) :
        return jsonify([1,2,3])

view = toma.as_view('mustapha')
app.add_url_rule('/alger' , view_func= view ,methods=['GET','POST'])

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/download')
def down():
    return send_from_directory(app.config["down"],path =app.config["down"], filename='zaki12.jpg', as_attachment=True)


@app.route('/ytb')
def yout() : 
    auth = request.authorization
    return 'algerien'


if __name__ == '__main__':
    app.run( debug=True)