from flask_restful import Resource, reqparse

# Defining the routes of the Application

'''
Registration
      # /api/v1/auth/registration
Login
      # /api/v1/auth/login

Get Collections
      # /api/v1/collections

Get collection
      # /api/v1/collection/<String:name>

Add Collection
      # /api/v1/collections

Remove collection
      # /api/v1/collection/<String:name>

Update collection name or video list
      # /api/v1/collection/<String:name>

Get Videos
      # /api/v1/videos/

Get Video
      # /api/v1/video/<String:name>

Add video
      # /api/v1/videos/

Delete video
      # /api/v1/videos/<String:name>
'''      


# /api/v1/auth/registration
class Registration(Resource):

      parser = reqparse.RequestParser()
      parser.add_argument('name', type=str, required=True, help='Name Cannot be empty')
      parser.add_argument('email', type=str, required=True, help='Email Cannot be empty')
      parser.add_argument('username', type=str, required=True, help='Username Cannot be empty')
      parser.add_argument('password', type=str, required=True, help='Password Cannot be empty')

      def post(self):
            auth_data  = Registration.parser.parse_args()
            
            name = auth_data['name']
            email = auth_data['email']
            username = auth_data['name']
            password = auth_data['password']

            # Calling the database function
            user_created,status_code = True, 301

            if user_created:
                  return {'message': 'Registration successful !'}, status_code
            return {'message': 'Registration failed !'}, status_code


# /api/v1/auth/login
class Login(Resource):

      parser = reqparse.RequestParser()
      parser.add_argument('username', type=str, required=True, help='Username Cannot be empty')
      parser.add_argument('password', type=str, required=True, help='Password Cannot be empty')

      def post(self):
            auth_data = Login.parser.parse_args()

            username = auth_data['username']
            password = auth_data['password']

            # Calling Database function
            is_user_exist, status_code = True, 404

            if is_user_exist:
                  # Call for JWT token creation
                  JWT_token = 'something'

                  return {'token': JWT_token}, status_code
            return {'message': 'Login unsuccessful due to invalid credintails'}, status_code


# /api/v1/collections
class Collections(Resource):

      parser = reqparse.RequestParser()
      parser.add_argument('name')
      parser.add_argument('videos')

      # Get the list of all collections
      def get(self):
            # Calling the database functions
            collections_data = []        
            return collections_data
      
      # Add the new collection to the list of collections
      def post(self):
            auth_data = Collections.parser.parse_args()

            name = auth_data['name']
            videos = auth_data['videos']

            # Call database function
            is_collection_created, status_code = True, 301

            if is_collection_created:
                  return {'message':f'Created the collection with {name}' }, 200
            return {'message': "Not Created"}, 400


# /api/v1/collection/<String:name>
class Collection(Resource):

      # Get the specific collection
      def get(self, name):
            collections_data = []
            return collections_data
      
      # Delete the specific collection
      def delete(self, name):
            deleted_item = 'item_deleted'
            return deleted_item

      # Update the collection name or collection videos
      def put(self, name):
            parser = reqparse.RequestParser()
            parser.add_argument('updated_name', type=str, required=False)
            parser.add_argument('updated_video_list', type=str, required=False)
            
            auth_data = parser.parse_args()
            response_message = {'message': 'Updated the provided data'}

            if 'updated_name' in auth_data:
                  # Call function to update name
                  response_message['updated_name'] = "some_message"
            if 'updated_video_list' in auth_data:
                  # Call function to update name
                  response_message['updated_video_list'] = "some_message"
            return response_message
                  

# /api/v1/videos/
class Videos(Resource):

      parser = reqparse.RequestParser()
      parser.add_argument('video')

      # Get the list of all videos
      def get(self):
            videos_list = []
            return videos_list
      
      # Add the new video to the list of video
      def post(self):
            auth_data = Videos.parser.parse_args()
            video = auth_data['video']

            # Call database function
            is_video_added, status_code = True, 301

            if is_video_added:
                  return {'message':'Added the video'}, 200
            return {'message': "Not Added"}, 400


# /api/v1/video/<String:name>
class Video(Resource):

      # Get the specific video
      def get(self, name):
            video_info = {}
            return video_info
      
      # Delete the specific video
      def delete(self, name):
            deleted_video = 'item_deleted'
            return deleted_video
