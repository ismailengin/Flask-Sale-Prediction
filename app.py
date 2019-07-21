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

]




# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#Flask-login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    flag = True
    print('aaaa')
    for u in USERS:
        if username not in u['id']:
            flag = False
    if (not flag):
        return
    user = User()
    user.id = username
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
            current_user = User()
            current_user.id = user['id']
            flask_login.login_user(current_user, True)
            print(flask_login.current_user)
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
@flask_login.login_required
def getTasks():
     return jsonify({
        'status': 'success',
        'tasks': TASKS
    })  

if __name__ == '__main__':
    app.secret_key = 'some secret key'
    app.run()