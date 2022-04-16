from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Flaskをインスタンス化している
app = Flask(__name__)
Bootstrap(app)

# デフォルトページの設定
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()