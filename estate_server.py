# python的岗位展示后端
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
import room_vector
import model
import estate
# 构建后端应用程序
server = Flask(__name__)
server.secret_key = 'your_secret_key'
# 先把后端的跨域问题解决
CORS(server, resources={r"/*": {"origins": "*"}})


# 定义一个提供月租金的数据的后端函数
@server.route("/rooms")
def rooms():
    connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from rooms limit 10"
    connect = connect.cursor()
    connect.execute(sql)
    rooms = connect.fetchall()
    return rooms


@server.route("/query_rooms")
def query_rooms():
    connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor)
    # 获取前端传递的参数
    min_price = request.args.get("min_price", type=float)  # 获取最低租金
    max_price = request.args.get("max_price", type=float)  # 获取最高租金
    sql = f"select * from clean_rooms where job_price >= {min_price} and job_price <= {max_price}"
    # 执行SQL查询
    with connect.cursor() as cursor:
        cursor.execute(sql)
        rooms = cursor.fetchall()
        return rooms


# 面积数量可视化后端函数
@server.route("/area_bar")
def area_bar():
    connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from area_statistics"
    cursor = connect.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    returndatas = []
    for data in datas:
        returndatas.append({"value": data['area_count'], "name": data['job_area']})
    return returndatas


# 月租金数量可视化函数
@server.route("/price_bar")
def price_bar():
    connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from price_statistics"
    cursor = connect.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    returndatas = []
    for data in datas:
        returndatas.append({"value": data['price_count'], "name": data['job_price']})
    return returndatas


# 房屋不同户型数量可视化
@server.route("/house_bar")
def house_bar():
    connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from house_statistics"
    cursor = connect.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    returndatas = []
    for data in datas:
        returndatas.append({"value": data['house_count'], "name": data['job_house']})
    return returndatas


# 房屋不同朝向数量可视化
@server.route("/orientation_bar")
def orientation_bar():
    connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from orientation_statistics"
    cursor = connect.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    returndatas = []
    for data in datas:
        returndatas.append({"value": data['orientation_count'], "name": data['job_orientation']})
    return returndatas


# 房屋不同朝向数量可视化
@server.route("/way_bar")
def way_bar():
    connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from way_statistics"
    cursor = connect.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    returndatas = []
    for data in datas:
        returndatas.append({"value": data['way_count'], "name": data['job_way']})
    return returndatas


# 定义后端路由，用来接受前端的推荐请求
@server.route('/recommand')
def demo():
    param_array = []
    # 岗位区域向量化进入数组
    job_address = request.args.get('job_address')
    room_vector.address_vec(job_address, param_array)
    # 岗位薪资向量化进入数组
    job_price = int(request.args.get("job_price"))
    room_vector.price_to_vec(job_price, param_array)
    # 岗位的学历和岗位的工作经验要向量化进入数组
    param_array.append(int(request.args.get('job_house')))
    param_array.append(int(request.args.get('job_way')))
    # 2、开发推荐算法，准备给前端返回的数据
    result = estate.recommand(param_array)
    # 3、返回数据
    return result


@server.route('/predict')
def demo1():
    # 1、接受前端传递的三个参数：户型  地区  租房方式
    param_array = []
    # 岗位的学历和岗位的工作经验要向量化进入数组
    param_array.append(int(request.args.get('job_house')))
    job_address = request.args.get('job_address')
    room_vector.address_vec(job_address, param_array)
    param_array.append(int(request.args.get('job_way')))
    # 岗位区域向量化进入数组

    # 将数组的每一项与model的每一项想成累加
    salary = 0
    for i in range(0, 3):
        salary += param_array[i] * model.model[i]
    return {'salary': salary}

############################################################################
# MySQL database connection
def get_db_connection():
    try:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="your_database",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.MySQLError as e:
        flash(f"数据库连接失败: {e}", "错误")
        return None
@server.route('/')
def login():
    return render_template('login_register.html')


@server.route("/register", methods=["GET", "post"])
def register():
    if request.method == "post":
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        try:
            connection = pymysql.connect(host='localhost', user='root', password='root', database='your_database')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            connection.commit()
            connection.close()
            flash('注册成功！', '成功')
            return redirect(url_for('login'))
        except pymysql.MySQLError as e:
            flash(f"注册失败: {e}", "错误")
            return render_template('login_register.html', register=True)


@server.route('/login', methods=['post'])
def user_login():
    username = request.form['username']
    password = request.form['password']
    if not username or not password:
        flash('用户名或密码不能为空。', '错误')
        return redirect(url_for('login'))
    conn = get_db_connection()
    if conn is None:
        flash('无法连接到数据库。', '错误')
        return redirect(url_for('login'))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user['password'], password):
        return redirect(url_for('dashboard'))
    else:
        flash('无效的凭证，请再试一次。', '错误')
        return redirect(url_for('login'))
@server.route('/dashboard')
def dashboard():
    return ""

if __name__ == '__main__':
    server.run(debug=True)
server.run()
