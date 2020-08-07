from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base route'

@app.route('/getallprojects/')
def get_all_projects():
    projects = ['BIED onderzoek September','Test onderzoek']
    message = {
        'status': 200,
        'message': 'OK',
        'content': projects
    }
    response = jsonify(projects)
    response.status_code = 200
    print(response)
    return response

@app.route('/getdatacollectionstatus/')
def get_data_collection_status():
    return 'Base route'
    
@app.route('/addtwitterhandle/')
def add_twitter_handle():
    return 'Base route'

@app.route('/getresults/')
def get_results():
    return 'Base route'

@app.route('/startproject/')
def start_project():
    return 'Base route'

@app.route('/deleteproject/')
def delete_project():
    return 'Base route'

if __name__ == '__main__':
    app.run()