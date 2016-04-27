from flask import Flask, render_template, request, session
import cgi
import datetime
import time
import json

app = Flask(__name__)
import pusher

#Settings
app.config['DEBUG'] = True
app.config['PUSHER_CHAT_APP_ID'] = '201481'
app.config['PUSHER_CHAT_APP_KEY'] = '1ebeb9579ca63bcb15eb'
app.config['PUSHER_CHAT_APP_SECRET'] = 'ac01089ec921da7d8b4c'
app.config['SECRET_KEY'] = '@\xb28\x12\x1b\xff\x1d\xcf\x1f](<\xd6\xe7\x9cH\xca\x94R\xf6V0\xf3\x10'

pusher_client = pusher.Pusher(
  app_id=app.config['PUSHER_CHAT_APP_ID'],
  key=app.config['PUSHER_CHAT_APP_KEY'],
  secret=app.config['PUSHER_CHAT_APP_SECRET'],
  ssl=True
)




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/setname/", methods=['POST'])
def set_name():
    session['name'] = request.form['name']
    return "Successful"

@app.route("/pusher/auth/",methods=['POST'])
def pusher_authentication():
    auth = pusher_client.authenticate(
        channel=request.form['channel_name'],
        socket_id=request.form['socket_id'],
        custom_data={
            'user_id':session['name']
        }
    )

    return json.dumps(auth)


@app.route("/messages/", methods=['POST'])
def new_message():
    name = request.form['name']
    text = cgi.escape(request.form['text'])
    channel = request.form['channel']

    now = datetime.datetime.now()
    timestamp = time.mktime(now.timetuple()) * 1000
    pusher_client.trigger("presence-"+channel,'new_message',{
        'text': text,
        'name': name,
        'time': timestamp
    })
    return "Successful!"


if __name__ == "__main__":
    app.run()
