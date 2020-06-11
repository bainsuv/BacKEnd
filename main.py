
import os
import json
import time
import pyodbc
import platform

from flask_cors import CORS
from flask import Flask, request
from data.database import cursor


app = Flask(__name__)
CORS(app)
 

@app.route("/", methods=['GET'])
def helloWorld():
    """
    http://127.0.0.1:5000
    """
    return json.dumps({'success': 'welcome to tweeter server!'})


@app.route("/login", methods=['GET'])
def login():
    """
    http://127.0.0.1:5000
    """
    username = request.args.get("username")
    password = request.args.get("password")
    #account = cursor.execute(f"select * from [dbo].[UserAccount] where username={username}")
    return json.dumps({'success': 'welcome to tweeter server!'})  

@app.route("/register", methods=['GET'])
def register():
    """
    http://127.0.0.1:5000/register?username=testuser3&password=suv78&email=dummymail@gmail.com
    """
    username = request.args.get("username")
    password = request.args.get("password")
    email    = request.args.get("email")
    """ f'insert into dbo.userAccount (username,password,email) values ({username},{password},{email}'
    """
    #cmd = "insert into dbo.UserAccount ([USER_NAME], [PASSWORD], Email) VALUES(" + username +"," + password +"," + email +")"
    #cursor.execute("insert into dbo.UserAccount ([USER_NAME], [PASSWORD], Email) VALUES ('Testuser2', 'password', 'testEmai@gmail.com’) ")
    account = cursor.execute("select * from [dbo].[UserAccount]")
    print(account)
    
    if account is None:
        return json.dumps({'success': 'false', 'message': 'Account Not Created'})
    return json.dumps({'success': 'true', 'message': 'Account Succesfully Created!'})



if __name__ == "__main__":
    if platform.system() == 'Linux':
        # Linux HOST
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port, threaded=True)
    else:
        # Windows HOST
        app.run(port=5000, debug=True, host='127.0.0.1')