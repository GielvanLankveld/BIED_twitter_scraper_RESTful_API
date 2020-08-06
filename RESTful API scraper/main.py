from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base route'

@app.route('/getallprojects/')
def hello_world():
    return 'Base route'

@app.route('/getdatacollectionstatus/')
def hello_world():
    return 'Base route'
    
@app.route('/addtwitterhandle/')
def hello_world():
    return 'Base route'

@app.route('/getresults/')
def hello_world():
    return 'Base route'

@app.route('/startproject/')
def hello_world():
    return 'Base route'

@app.route('/deleteproject/')
def hello_world():
    return 'Base route'

if __name__ == '__main__':
    app.run()