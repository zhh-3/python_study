from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)


@app.route('/')
def search():
    return render_template("index.html")

@app.route('/api', methods=["GET", "POST"])
def api():
    if request.method == "POST":
        print(request.form)
        dc = request.form.to_dict()
        print(dc)
        job = dc["job"]
        print(job)
        data = {}
        data["filename"] = job+"out.png"
        data["filename2"] = job+".png"
        return jsonify(data)

@app.route("/get_img/", methods=["GET", "POST"])
def test2():
            basepath = "F:\Python\pythoncode\jobInfo\main\\" # 当前文件所在路径
            if request.args.get("filename") == None: return jsonify({"error": 1001, "msg": ""})
            filename = basepath  + request.args.get("filename")
            print(filename)
            image_data = open(filename, "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


if __name__ == '__main__':
    app.run(host="5000", debug=True)
