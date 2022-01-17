from flask import Flask
import settings
# 导入蓝图
from app.user.view import user_bp

def create_app():
    app = Flask(__name__)

    # 绑定配置
    app.config.from_object(settings)

    # 蓝图绑定
    app.register_blueprint(user_bp)
    print(app.url_map)

    return app