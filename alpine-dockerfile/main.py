from flask import Flask
 
# 创建Flask实例
app = Flask(__name__)
 
# 定义接口路由
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'
 
if __name__ == '__main__':
    # 运行Flask应用
    app.run(debug=True)
