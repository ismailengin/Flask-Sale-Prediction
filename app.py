from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
import flask_login
from werkzeug import secure_filename

USERS = [
    {
        'id' : uuid.uuid4().hex,
        'username': 'a',
        'password': '123',
    }
]

TASKS = [
    pass

]




# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#Flask-login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(username):
    flag = True
    for u in USERS:
        if username not in u['username']:
            flag = False
    if (not flag):
        return
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.data.get('username')
    flag = True
    for u in USERS:
        if username not in u['username']:
            flag = False
    if (not flag):
        return
    user = User()
    user.id = username

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.data['password'] == USERS[username]['password']

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
    for user in USERS:
        if (user['username'] == uname and pw == user['password']):
             response_object['message'] = 'authenticated'
    return jsonify(response_object)

@app.route('/register', methods=['POST'])
#TODO: Passwordlari hashle
def register():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    uname = post_data.get("username")
    pw = post_data.get("password")
    flag = False
    for user in USERS:
        if (user['username'] == uname):
             response_object['message'] = 'exist'
             flag = True
             break
    if not flag:
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
def getTasks():
     return jsonify({
        'status': 'success',
        'tasks': TASKS
    })  

if __name__ == '__main__':
    app.run()