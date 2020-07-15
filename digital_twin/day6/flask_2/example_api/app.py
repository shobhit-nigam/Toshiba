#!flask/bin/python
from flask import Flask, request
from flask import jsonify, abort, make_response
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)

tasks = [
        {
            'id':21,
            'title' : 'do python exercises',
            'description' : 'finish part 1exercises by the=is week',
            'done':False
            },
        {
            'id' : 22,
            'title' : 'status meet',
            'description' : 'prepare report for status meet',
            'done':False
            },
        ]

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'tsip':
        return 'tsip123'
    else:
        return None

@auth.error_handler
def perm_denied():
    return make_response(jsonify({'error':'permission denied'}), 401)


@app.route('/ex/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_tasks(task_id):
    task = []
    for t in tasks:
        if t['id'] == task_id:
            task.append(t)

    if len(task) == 0:
        abort(404)

    return jsonify({'tasks':task[0]})


@app.route('/ex/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'], 
            'description': request.json.get('description', ""),
            'done':False
            }
    tasks.append(task)
    return jsonify({'task':task}), 201


@app.route('/ex/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/ex/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def error_not_found(error):
    return make_response(jsonify({'error':'list not found'}), 404)


@app.route('/')
def index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)
