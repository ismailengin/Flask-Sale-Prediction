from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import uuid
from werkzeug import secure_filename
from flask_jwt_extended import create_access_token, JWTManager
import LSTM
from threading import Thread


TASKS = [
    {'id': '02cc3989e4574e03a29756b530415edc', 'owner': 'a', 'filename': 'dataset.csv', 'taskname': 'asdad', 'predictionStep': '5'}
]

RESULTS = [

]
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

jwt = JWTManager(app)

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
    else:
        result = jsonify({"error": "Invalid username and password"}) 
    print(result)   
    return result

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
        
    else:
        response_object['message'] ='exist'     
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
    owner = request.form.get('taskowner')
    TASKS.append({
        'id': uuid.uuid4().hex,
        'owner':  owner,
        'filename': xfile.filename,
        'taskname': taskname,
        'predictionStep': step,
        'predicted': False
    })
    response_object['message'] = 'added'
    return jsonify(response_object)  

@app.route('/getTasks', methods=['POST'])
def getTasks():
    owner = request.form.get('owner')
    return jsonify({
        'status': 'success',
        'tasks': [task for task in TASKS if task['owner'] == owner],
    })

@app.route('/predict/<task_id>', methods=['PUT'])
def predict(task_id):
    RESULTS.append({
        'task_id': task_id,
        'status': False
    })
    index = 0
    for i in range(0, len(TASKS)):
        if task_id == TASKS[i]['id']:
            index = i
            break
    task = TASKS[index]
    print(task['filename'])
    t1 = Thread(target=LSTM.calculate_predict, args=[task_id, task['filename'], task['predictionStep'], RESULTS])
    t1.start()
    t1.join()
    result_index = 0
    for i in range(0, len(RESULTS)):
        if task_id == RESULTS[i]['task_id']:
            result_index = i
            break
    if RESULTS[result_index]['status'] == True:
        TASKS[index]['predicted'] = True
    print(TASKS)   
    return jsonify({
        'status': 'success',
        #'tasks': [task for task in TASKS if task['owner'] == owner],
    })

@app.route('/show/<task_id>', methods=['GET'])
def show_task_result(task_id):
    return send_from_directory('results', task_id+'.png')

if __name__ == '__main__':
    app.secret_key = 'some secret key'
    app.run()