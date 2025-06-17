from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        msg = request.form['message']
        new_msg = Message(text=msg)
        db.session.add(new_msg)
        db.session.commit()
        return redirect('/messages')
    all_msgs = Message.query.all()
    return render_template('messages.html', messages=all_msgs)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
