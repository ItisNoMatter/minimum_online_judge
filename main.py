from flask import Flask,request
import os
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] ="./uploads"

new_id = 0

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/upload",methods=["POST"])
def upload():
    uploaded_file = request.files.get("file")
    save_path = store_file(uploaded_file)
    if uploaded_file is None or uploaded_file.filename == '':
        return "No file uploaded", 400
    return f"Saved file to {save_path}"


def store_file(uploaded_file):
    global new_id

    dir_path = os.path.join(app.config["UPLOAD_FOLDER"], str(new_id))
    os.makedirs(dir_path, exist_ok=True)
    
    save_path = os.path.join(dir_path,uploaded_file.filename)
    
    uploaded_file.save(save_path)
    return save_path

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8005)
