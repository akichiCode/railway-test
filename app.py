from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Railway! 🚂</h1><p>Railwayでのデプロイが成功しました！</p>'

@app.route('/test')
def test():
    return {'message': 'API動作確認OK', 'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)