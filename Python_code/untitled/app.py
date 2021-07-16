from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return '你好python!'


@app.route('/test')
def hello():
    return 'python!'


@app.route('/utf')
def world():
    return '你好!'

@app.route('/user=<name>')
def hi(name):
    return '你好%s!' % name


# 传入参数为整形
@app.route('/id=<int:id>')
def hi2(id):
    return '你好%d!' % id


# 返回给用户渲染后的网页文件
@app.route('/')
def index2():
    return render_template("index.html")


@app.route('/arg')
def index3():
    time = datetime.date.today()
    names = ["张", "王", "李", "赵"]
    tasks = {"任务": "打扫卫生", "时间": "3小时"}
    return render_template("index.html", var = time, names = names, tasks = tasks)

@app.route('/test/register')
def register():
    return render_template("test/register.html")


@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == 'POST':
        respond = request.form
        return render_template("test/result.html", respond = respond)


if __name__ == '__main__':
    app.run()
