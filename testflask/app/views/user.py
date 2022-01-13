from flask import Blueprint,jsonify,request
from ..utils.sql import db_conn
import os
import time

# 蓝图，account.py所有的路由前面都必须加/admin,如127.0.0.1:5050/admin/login
us = Blueprint('us',__name__)

