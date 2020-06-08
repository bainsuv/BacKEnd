
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
    account = cursor.execute(f'select * from [dbo].[UserAccount] where username= {username}')
    return json.dumps({'success': 'welcome to tweeter server!'})  



@app.route("/GetAllUserAccounts", methods=['GET'])
def GetAllUserAccounts():
    """
    http://127.0.0.1:5000/GetAllUserAccounts
    """
    return cursor.execute('select * from [dbo].[UserAccount]').fetchall()



if __name__ == "__main__":
    if platform.system() == 'Linux':
        # Linux HOST
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port, threaded=True)
    else:
        # Windows HOST
        app.run(port=5000, debug=True, host='127.0.0.1')