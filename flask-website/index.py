from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'This is index.py: Hello World'

app.run(host='0.0.0.0')

if __name__ == '__main__':
   app.run()