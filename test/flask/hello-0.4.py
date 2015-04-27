from flask import Flask
app = Flask(__name__)


@app.route('/')
def get_info():
    return 'Hello World!'

@app.route('/config')
def config_server():
    return 'Configurate server!'

@app.route('/status')
def get_status():
    return 'Get status!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
