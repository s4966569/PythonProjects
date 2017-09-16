from flask import Flask
from flask import render_template
from flask import request

from MYSQLHelper import MYSQLHelper
app = Flask(__name__)


@app.route('/')
def index():
    dbhelper = MYSQLHelper()
    data = dbhelper.query_replies()
    return render_template('add_user.html',data=data)


@app.route('/post_user', methods=['GET','POST'])
def post_user():
    username = request.form['username']
    email = request.form['email']
    return "用户名:" + username + "密码:" + email


if __name__ == '__main__':
    app.run()
