from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
import flask_login
from werkzeug import secure_filename


TASKS = [

]




# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#Flask-login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

#Flask-JWT

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

USERS = [
    User(uuid.uuid4().hex, 'a', '123')
]

username_table = {u.username: u for u in USERS}
userid_table = {u.id: u for u in USERS}



def authenticate(username, password):
    print('aaaa')
    user = username_table.get(username, None)
    if user and password == user.password:
        return user


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/authenticate', methods=['POST'])
def login():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    uname = post_data.get("username")
    pw = post_data.get("password")
    user = authenticate(uname,pw)
    if user:
        access_token = create_access_token(
            identity={
                'id': user.id,
            })
        result = access_token    
        #response_object['message'] = 'authenticated'

@app.route('/register', methods=['POST'])
#TODO: Passwordlari hashle
def register():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    uname = post_data.get("username")
    pw = post_data.get("password")
    flag = False
    user = username_table.get(uname, None)
    if not user:
        USERS.append({
            'id': uuid.uuid4().hex,
            'username': uname,
            'password': pw,
        })
        response_object['message'] = 'added'
    return jsonify(response_object)

@app.route('/getusers', methods=['GET'])
def allUsers():
     return jsonify({
        'status': 'success',
        'users': USERS
    })   

@app.route('/createTask', methods=['POST'])
def createTask():
    #TODO: Check if file exists with hash control
    response_object = {'status': 'success'}
    taskname = request.form.get('taskname')
    xfile = request.files.get('file')
    xfile.save(secure_filename(xfile.filename))
    step = request.form.get('step')
    TASKS.append({
        'id': uuid.uuid4().hex,
        'filename': xfile.filename,
        'taskname': taskname,
        'predictionStep': step
    })
    response_object['message'] = 'added'
    return jsonify(response_object)  

@app.route('/getTasks', methods=['GET'])
@flask_login.login_required
def getTasks():
     return jsonify({
        'status': 'success',
        'tasks': TASKS
    })  

if __name__ == '__main__':
    app.secret_key = 'some secret key'
    app.run()