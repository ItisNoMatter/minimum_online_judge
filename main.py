from flask import Flask

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] ="./uploads"


@app.route('/')
def index():
    return 'Hello World!'


@app.route("/upload",methods=["POST"])
def upload():
    return "aaa"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8005)
