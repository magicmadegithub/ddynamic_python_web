from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

# 静态文件目录的路径 默认当前项目中的static目录
static_folder = 'static'

# 静态文件目录的url路径 默认不写是与static_folder同名,远程静态文件时复用
static_url_path = None,

# template模板目录, 默认当前项目中的 templates 目录
template_folder = 'templates'

resource = {
    "ids": [
        {
            "id": "homePageId003",
            "version": "0.0.1",
            "sdkVersion": "0.0.1",
            "appVersion": "1.0.0",
            "exeTime": 1598067358000,
            "downloadUrl": "http://122.51.125.14:5000/static/resource03.zip"
        },
    ],
    "deleteIds": [
        {
            "id": "homePageId001",
            "version": "0.0.1",
        },
        {
            "id": "homePageId002",
            "version": "0.0.1",
        },
    ]
}


@app.route('/dynamicResource', methods=['POST'])
def get_resource():
    return jsonify(resource)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
