from flask import Blueprint,jsonify
from ..utils.sql import db_conn

# 蓝图，account.py所有的路由前面都必须加/admin,如127.0.0.1:5050/admin/login
ac = Blueprint('ac',__name__,url_prefix='/admin')

@ac.route('/login',methods=['POST','GET'])
def login():
    return 'login'