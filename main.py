from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! ii 77 lk mm llmmmll iii'


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0',port=3001,debug=True)