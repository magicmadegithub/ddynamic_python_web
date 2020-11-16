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
            "exeTime": 1597983901000,
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

refresh = {
    "base_info": {
        "name": "李四-李四",
        "grade": 5,
        "grade_name": "高二",
        "service_days": 2757,
        "remaining_class_hours": 8039,
        "total_buy_class_hours": 6831
    },
}

class_week = {
    "error_code": 0,
    "message": "msg",
    "result": {
        "biz_product_line": 1,
        "semester_end_time": "2020.12.12",
        "semester_begin_time": "2020.10.19",
        "course_frequency": 2,
        "rule_count": 1,
        "avg_teacher": 10,
        "week_teacher_time": [
            {
                "week": 0,
                "period_time_teacher": [
                    {
                        "period_time": "08:00-09:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "10:00-11:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "13:00-14:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "15:00-16:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:00-20:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "17:30-21:25",
                        "adequate": 1
                    },
                    {
                        "period_time": "18:00-21:55",
                        "adequate": 2
                    }
                ]
            },
            {
                "week": 1,
                "period_time_teacher": [
                    {
                        "period_time": "08:00-09:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "10:00-11:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "13:00-14:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "15:00-16:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "17:00-20:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:30-21:25",
                        "adequate": 1
                    },
                    {
                        "period_time": "18:00-21:55",
                        "adequate": 1
                    }
                ]
            },
            {
                "week": 2,
                "period_time_teacher": [
                    {
                        "period_time": "08:00-09:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "10:00-11:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "13:00-14:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "15:00-16:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:00-20:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "17:30-21:25",
                        "adequate": 1
                    },
                    {
                        "period_time": "18:00-21:55",
                        "adequate": 2
                    }
                ]
            },
            {
                "week": 3,
                "period_time_teacher": [
                    {
                        "period_time": "08:00-09:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "10:00-11:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "13:00-14:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "15:00-16:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:00-20:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:30-21:25",
                        "adequate": 1
                    },
                    {
                        "period_time": "18:00-21:55",
                        "teacher_num": 2
                    }
                ]
            },
            {
                "week": 4,
                "period_time_teacher": [
                    {
                        "period_time": "08:00-09:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "10:00-11:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "13:00-14:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "15:00-16:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:00-20:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "17:30-21:25",
                        "adequate": 1
                    },
                    {
                        "period_time": "18:00-21:55",
                        "adequate": 2
                    }
                ]
            },
            {
                "week": 5,
                "period_time_teacher": [
                    {
                        "period_time": "08:00-09:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "10:00-11:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "13:00-14:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "15:00-16:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:00-20:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "17:30-21:25",
                        "adequate": 2
                    },
                    {
                        "period_time": "18:00-21:55",
                        "adequate": 2
                    }
                ]
            },
            {
                "week": 6,
                "period_time_teacher": [
                    {
                        "period_time": "08:00-09:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "10:00-11:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "13:00-14:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "15:00-16:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "17:00-20:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "17:30-21:25",
                        "adequate": 25
                    },
                    {
                        "period_time": "18:00-21:55",
                        "adequate": 1
                    }
                ]
            }
        ]
    }
}

class_day = {
    "error_code": 0,
    "message": "msg",
    "result": {
        "biz_product_line": 1,
        "semester_end_time": "2020.12.24",
        "semester_begin_time": "2020.9.19",
        "course_frequency": 1,
        "rule_count": 1,
        "avg_teacher": 15,
        "week_teacher_time": [
            {
                "week": 3,
                "period_time_teacher": [
                    {
                        "period_time": "08:00-09:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "10:00-11:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "13:00-14:55",
                        "adequate": 1
                    },
                    {
                        "period_time": "15:00-16:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:00-20:55",
                        "adequate": 2
                    },
                    {
                        "period_time": "17:30-21:25",
                        "adequate": 1
                    },
                    {
                        "period_time": "18:00-21:55",
                        "teacher_num": 2
                    }
                ]
            }
        ]
    }
}


@app.route('/dynamicResource', methods=['POST'])
def get_resource():
    return jsonify(resource)


@app.route('/dynamicRefresh', methods=['GET'])
def get_refresh():
    return jsonify(refresh)


@app.route('/classWeek', methods=['GET'])
def get_class_week():
    return jsonify(class_week)


@app.route('/classDay', methods=['GET'])
def get_class_day():
    return jsonify(class_day)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
