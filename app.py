from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # API を呼び出してデータを取得
    api_url = 'http://word-of-the-day-git.openshift-tempo-operator.svc:8081'
    response = requests.get(api_url)
    data = response.json()

    # 取得したデータをテンプレートに渡してレンダリング
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

