from flask import Flask

app = Flask(__name__)

@app.route('/main')
def main():
    return {'code': 200, 'message': 'hello'}

if __name__ == '__main__':
    app.run()
