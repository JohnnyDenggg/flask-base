from flask import Flask,jsonify,send_from_directory,request
from .utils.sql import db_conn
import os
import time

app = Flask(__name__)

# jsonfy显示中文
app.config['JSON_AS_ASCII']=False

# 添加蓝图
from .views import account
from .views import user

app.register_blueprint(account.ac)
app.register_blueprint(user.us)

############ 数据库pymysql 示例  ########################

# 查数据 并显示为 键:值 的形式，用json形式返回
@app.route('/',methods=['POST','GET'])
def index():
    sql = 'SELECT * FROM test;'
    res = db_conn(sql)
    if res:
        data = {'code': 200, 'list': res}
        return jsonify(data)
    else:
        return jsonify({'code':400})

# 查特定数据 Postman:  localhost:5050/search?role=boss&id=1&name=deng
@app.route('/search',methods=['POST','GET'])
def cha():
    name = request.args.get('name')
    res = db_conn("SELECT * FROM test WHERE name=%s",name)
    if res:
        print(res)
        data = {'code': 200, 'list': res}
        return jsonify(data)
    else:
        return jsonify({'code': 400})

# 删 Postman:  localhost:5050/delete?role=boss&id=1&name=hua
@app.route('/delete',methods=['POST','GET'])
def shan():
    id = request.args.get('id')
    name = request.args.get('name')
    password = request.args.get('password')
    role = request.args.get('role')
    res = db_conn("DELETE FROM test WHERE name=%s",name)
    print(res)
    if res:
        return jsonify({'code':200})
    else:
        return jsonify({'code':400})

# 增 Postman:  localhost:5050/add?role=employee&password=000&name=zhao
@app.route('/add',methods=['POST','GET'])
def tianjia():
    name = request.args.get('name')
    password = request.args.get('password')
    role = request.args.get('role')
    print(name,password,role)
    res = db_conn("INSERT INTO test (name,password,role) VALUES (%s,%s,%s)",[name,password,role])
    if res:
        return jsonify({'code':200})
    else:
        return jsonify({'code':400})

# 改 Postman:  localhost:5050/modify?role=Manager&password=456&id=2&name=zhong
@app.route('/modify',methods=['POST','GET'])
def gai():
    id = request.args.get('id')
    name = request.args.get('name')
    password = request.args.get('password')
    role = request.args.get('role')
    print(id,name,password,role)
    res = db_conn("UPDATE test SET name=%s,password=%s,role=%s WHERE id=%s",[name,password,role,id])
    if res:
        return jsonify({'code':200})
    else:
        return jsonify({'code':400})

# 上传图片
@app.route('/upload',methods=['POST','GET'])
def shangchuan():
    type = request.args.get('type')
    image = request.files.get('image')  ### y这里有问题，上传图片，flask验证码登陆
    print(time.time())
    if image and type:
        image.save("./app/uploads/image/" + type + '/' + str(time.time()) + image.filename)
        return jsonify({'code': 200})
    else:
        return jsonify({'code': 400})


# 显示图片
@app.route('/image/<filename>',methods=['POST','GET'])
def tupian(filename):
    basepath = os.path.dirname(__file__)
    UPLOAD_PATH = os.path.join(basepath, 'uploads/avatar')
    return send_from_directory(UPLOAD_PATH, filename)

