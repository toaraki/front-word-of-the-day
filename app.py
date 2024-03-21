from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # API を呼び出してデータを取得
    api_url = 'http://word-of-the-day-git.openshift-tempo-operator.svc:8081/rolldice'
    response = requests.get(api_url)

    print("Backend Response:", response.text)
    
    # JSON データの取得に成功した場合
    if response.status_code == 200:
        data = response.json()
    else:
        # エラーが発生した場合は空のデータを使用する
        data = {}
    
    # 取得したデータをテンプレートに渡してレンダリング
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

