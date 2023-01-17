from flask import Flask, render_template, request, redirect
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
  # 掲示板データファイルを開く
  try:
    with open('/var/python-app/data.txt') as f:
      lines = f.read() #内容を読み込む
  except IOError:
    # ファイルが存在しない場合は空文字列にする
    lines = ""
  # ファイルから読み込んだデータをhtmlに渡す
  return render_template('index.html', data = lines.split("\n"))

@app.route('/', methods=["POST"])
def index_post():
  name = request.form["name"]
  msg = request.form["msg"]
  time = datetime.now()
  
  with open('/var/python-app/data.txt', 'a') as f:
    f.write(f"{time} {name} {msg}\n")
  
  return redirect("/")

if __name__ == '__main__':
  # フォルダの作成
  os.makedirs("/var/python-app", exist_ok=True)
  # Flaskの起動
  app.run(host='0.0.0.0', port=5000, debug=True)
