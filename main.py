from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('auth/register.html')

if __name__ == "__main__":
    app.run()

#Ingat:
#1. Jalankan '. venv/bin/activate'
#2. 'python -m venv venv'
#3. 'export FLASK_APP=main.py'
#4. 'flask run'

#https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/
