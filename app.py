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
    "course_frequency": 2,
    "semester_begin_time": 1582214400,
    "semester_end_time": 1593705599,
    "week_teacher_time": [
      {
        "week": 1,
        "period_time_teacher": [
          {
            "period_time": "08:00-09:55",
            "scene_id": 1,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "10:30-12:25",
            "scene_id": 2,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "13:30-15:25",
            "scene_id": 3,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "16:00-17:55",
            "scene_id": 4,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "17:00-18:55",
            "scene_id": 5,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "17:30-19:25",
            "scene_id": 6,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "18:00-19:55",
            "scene_id": 7,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "18:30-20:25",
            "scene_id": 8,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:00-20:55",
            "scene_id": 9,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:30-21:25",
            "scene_id": 10,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "20:00-21:55",
            "scene_id": 11,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          }
        ]
      },
      {
        "week": 2,
        "period_time_teacher": [
          {
            "period_time": "08:00-09:55",
            "scene_id": 1,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "10:30-12:25",
            "scene_id": 2,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "13:30-15:25",
            "scene_id": 3,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "16:00-17:55",
            "scene_id": 4,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "17:00-18:55",
            "scene_id": 5,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "17:30-19:25",
            "scene_id": 6,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "18:00-19:55",
            "scene_id": 7,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "18:30-20:25",
            "scene_id": 8,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:00-20:55",
            "scene_id": 9,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:30-21:25",
            "scene_id": 10,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "20:00-21:55",
            "scene_id": 11,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          }
        ]
      },
      {
        "week": 3,
        "period_time_teacher": [
          {
            "period_time": "08:00-09:55",
            "scene_id": 12,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "10:30-12:25",
            "scene_id": 13,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "13:30-15:25",
            "scene_id": 14,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "16:00-17:55",
            "scene_id": 15,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "17:00-18:55",
            "scene_id": 16,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "17:30-19:25",
            "scene_id": 17,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "18:00-19:55",
            "scene_id": 18,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "18:30-20:25",
            "scene_id": 19,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:00-20:55",
            "scene_id": 20,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "19:30-21:25",
            "scene_id": 21,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "20:00-21:55",
            "scene_id": 22,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          }
        ]
      },
      {
        "week": 4,
        "period_time_teacher": [
          {
            "period_time": "08:00-09:55",
            "scene_id": 23,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "10:30-12:25",
            "scene_id": 24,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "13:30-15:25",
            "scene_id": 25,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "16:00-17:55",
            "scene_id": 26,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "17:00-18:55",
            "scene_id": 27,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "17:30-19:25",
            "scene_id": 28,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "18:00-19:55",
            "scene_id": 29,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "18:30-20:25",
            "scene_id": 30,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:00-20:55",
            "scene_id": 31,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:30-21:25",
            "scene_id": 32,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "20:00-21:55",
            "scene_id": 33,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          }
        ]
      },
      {
        "week": 5,
        "period_time_teacher": [
          {
            "period_time": "08:00-09:55",
            "scene_id": 34,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "10:30-12:25",
            "scene_id": 35,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "13:30-15:25",
            "scene_id": 36,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "16:00-17:55",
            "scene_id": 37,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "17:00-18:55",
            "scene_id": 38,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "17:30-19:25",
            "scene_id": 39,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "18:00-19:55",
            "scene_id": 40,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "18:30-20:25",
            "scene_id": 41,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "19:00-20:55",
            "scene_id": 42,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:30-21:25",
            "scene_id": 43,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "20:00-21:55",
            "scene_id": 44,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          }
        ]
      },
      {
        "week": 6,
        "period_time_teacher": [
          {
            "period_time": "08:00-09:55",
            "scene_id": 45,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "10:30-12:25",
            "scene_id": 46,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "13:30-15:25",
            "scene_id": 47,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "16:00-17:55",
            "scene_id": 48,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:00-20:55",
            "scene_id": 49,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "19:30-21:25",
            "scene_id": 50,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "20:00-21:55",
            "scene_id": 51,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          }
        ]
      },
      {
        "week": 0,
        "period_time_teacher": [
          {
            "period_time": "08:00-09:55",
            "scene_id": 52,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "10:30-12:25",
            "scene_id": 53,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "13:30-15:25",
            "scene_id": 54,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "16:00-17:55",
            "scene_id": 55,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:00-20:55",
            "scene_id": 56,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          },
          {
            "period_time": "19:30-21:25",
            "scene_id": 57,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 1
          },
          {
            "period_time": "20:00-21:55",
            "scene_id": 58,
            "teacher_num": 0,
            "totalTeachers": 1358,
            "adequate": 0
          }
        ]
      }
    ],
    "rule_count": 2,
    "avg_teacher": 20
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
