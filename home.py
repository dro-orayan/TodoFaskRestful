#import libraries
from flask import Flask
from flask_restful import Api, Resource,reqparse, abort

#set "app" as variable. Flask as the module
app = Flask(__name__)
api = Api(app)

#Database
TODOS = {
    'todo1' :{'task': 'Install Requirements.txt'},
    'todo2' :{'task': 'Install Requirements.txt'},
    'todo3' :{'task': 'Install Requirements.txt'}
}

# Create a parser for incoming JSON data
parser = reqparse.RequestParser()


#Create Class/Resources
class Todo(Resource):
    def get(self, todo_id):
        return TODOS[todo_id], 200
    
    def delete(self, todo_id):
        del TODOS[todo_id]
        return'', 201
    
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
    
class TodoList(Resource):
    
    def post():
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = "todo%i" % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
    

if __name__ == '__main__':
    app.run(debug=True)