from .app import app  # 从 app文件夹导入__init__.py里的 app


if __name__ == '__main__':
    app.run(debug=True)