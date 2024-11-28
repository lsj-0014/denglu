'''
预测模型的训练构建代码
模型的数学原理：多元线性方程组的系数矩阵的求解
        已知 因变量矩阵y和自变量矩阵x，求解系数矩阵 β
        求解公式： β = （x.T * x）^-1 * x.T * y
求解模型就是求解β系数矩阵
需要先把x和y矩阵构建出来
'''
import pymysql
import numpy as np
import room_vector

# x m行n列的矩阵  其中每一行代表一条岗位信息的xn的值
x = [] # 存放自变量矩阵的值
# y 一行n列
y = [] # 存放因变量矩阵的值

# 连接数据库查询数据
connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room", charset='utf8', cursorclass=pymysql.cursors.DictCursor)
sql = "select * from clean_rooms"
curses = connect.cursor()
curses.execute(sql)
# 这就是数据库查询回来的全部数据
jobs = curses.fetchall()
connect.close()

'''
在真实的算法开发领域，我们需要先做一件事情，把数据拆分开，  8:训练  2:测试评估
'''
'''
数据处理成为特征向量，加到对应的自变量矩阵和因变量矩阵
'''
for job in jobs:
    # 把薪资放到因变量的矩阵中
    y.append(int(job['job_price']))
    # 自变量矩阵  每一行的数据处理矩阵：类型、学历、工作经验、地区
    job_juzhen = room_vector.jobs_vec(job)
    x.append(job_juzhen)

# 将数组处理成为矩阵
x_mat = np.array(x) # 自变量矩阵
y_mat_T = np.array(y) # 因变量的转置矩阵
y_mat = y_mat_T.T
# 最小二乘法的求解公式运算  模型求解
b = np.linalg.inv(x_mat.T.dot(x_mat)).dot(x_mat.T).dot(y_mat)

# 将系数矩阵转换成为数组，保存到一个py文件中，供预测使用
b_array = []
for i in range(len(b)):
    b_array.append(float(b[i]))
# 保存模型供后期的预测使用
file = open("model.py", "w")
file.write("model="+str(b_array))
print(b_array)