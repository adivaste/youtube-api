import os
from routes import Registration, Login, Collections, Collection, Videos, Video

from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

# Loading the enviroment variable 
load_dotenv()


# Creating the Flask Application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
api = Api(app)


# Defining the routes of the Application

# Registraction   :  /api/v1/auth/registration         : Registration
# Login           :  /api/v1/auth/login                : Login
# Collections     :  /api/v1/collections               : Get collections, Add collection
# Collection      :  /api/v1/collection/<String:name>  : Get collection, Delete collection, Update collection
# Videos          :  /api/v1/videos/                   : Get videos, Add videos
# Video           :  /api/v1/video/<String:name>       : Get video, Delete video


api.add_resource(Registration, '/api/v1/auth/registration')
api.add_resource(Login, '/api/v1/auth/login')
api.add_resource(Collections, '/api/v1/collections')
api.add_resource(Collection, '/api/v1/collection/<string:name>')
api.add_resource(Videos, '/api/v1/videos')
api.add_resource(Video, '/api/v1/video/<string:name>')


# Configuring the Flask Application and starting it 
if __name__ == '__main__':
      app.run(port=8080, debug=True)