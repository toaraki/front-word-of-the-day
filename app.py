from flask import Flask, render_template, jsonify
import requests
from opentelemetry import trace
from opentelemetry import metrics
import logging


# Acquire a tracer
tracer = trace.get_tracer("diceroller.tracer")
# Acquire a meter.
meter = metrics.get_meter("diceroller.meter")

# Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
  "front",
   description="Front page of this suite"
)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    # API を呼び出してデータを取得
    api_url = 'http://app-wotd:8081/rolldice'
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

