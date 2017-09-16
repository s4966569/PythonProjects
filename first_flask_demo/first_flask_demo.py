from flask import Flask
from flask import render_template
from flask import request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from MYSQLHelper import MYSQLHelper
from SQLALchemyHelper import SQLALchemyHelper
from ReplyInfo import ReplyInfo
from Pet import Pet

app = Flask(__name__)

session = SQLALchemyHelper().session

@app.route('/')
def index():
    dbhelper = MYSQLHelper()
    data = dbhelper.query_replies(100)
    dbhelper.closedb()
    # data = session.query(ReplyInfo).all()
    # session.commit()
    return render_template('add_user.html',data=data)


@app.route('/post_user', methods=['GET','POST'])
def post_user():
    username = request.form['username']
    email = request.form['email']
    return "用户名:" + username + "密码:" + email


@app.route('/profile/<petname>')
def profile(petname):
    pet = session.query(Pet).filter_by(name=petname).one()
    session.commit()
    return render_template('profile.html',pet=pet)

if __name__ == '__main__':
    app.run()
