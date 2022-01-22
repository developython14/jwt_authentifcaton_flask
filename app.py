from distutils.log import debug
from flask import Flask, jsonify , render_template, request ,url_for
from flask import send_file, send_from_directory, safe_join, abort
import os 
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager




app = Flask(__name__)
main_path = os.path.dirname(os.path.abspath(__file__)) 
app.config["down"] =os.path.join(main_path,'images')  


# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)



# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200




@app.route("/")
def hello_world():
    return render_template('index.html')




@app.route('/download')
def down():
    return send_from_directory(app.config["down"],path =app.config["down"], filename='zaki12.jpg', as_attachment=True)







if __name__ == '__main__':
    app.run( debug=True)