from flask import Flask
from views import testFunction
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(testFunction.test_function)
CORS(app)

def main():
    app=Flask(__name__)
    app.run()
#debug=True,host='',port=''

if __name__=='__main__':
    main()