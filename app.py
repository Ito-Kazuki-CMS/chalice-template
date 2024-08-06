from chalice import Chalice
from chalice import NotFoundError

app = Chalice(app_name='chaliceApp')

# /api
@app.route('/')
def index():
    return {'text': 'Hello world!!', 'pattern': 1}

# /api/test
@app.route('/test')
def index():
    return {'hello': 'world-test'}

# /api/hello/test-name-1
@app.route('/hello/{name}')
def hello_name(name):
   return {'hello': name}

# /api/users
# json:{"id":100, "name":"test-san"}
# jsonで設定した内容が設定された状態でレスポンスが返ってくる
@app.route('/users', methods=['POST'])
def create_user():
    user_as_json = app.current_request.json_body
    return {'user': user_as_json}

# /api/objects/key-1
# json:{"id":100, "name":"test-san"}
# URLにキーを、jsonに本体を設定しPUT
# GET時のURLに設定したキーを元にPUTしたJsonを取得する
OBJECTS = {
}

@app.route('/objects/{key}', methods=['GET', 'PUT'])
def myobject(key):
    request = app.current_request
    if request.method == 'PUT':
        OBJECTS[key] = request.json_body
    elif request.method == 'GET':
        try:
            return {key: OBJECTS[key]}
        except KeyError:
            raise NotFoundError(key)