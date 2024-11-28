'''
获取数据库所有的清洗完成的岗位数据
把每一个岗位数据向量化，和参数向量化求一个向量的余弦值
判断如果余弦值大于0.8 代表岗位可以推荐。岗位加入到一个数组中，准备给前端返回
'''
import numpy as np
import pymysql
import room_vector
def recommand(param_array):
    # 定义一个数组，存放推荐的数据
    recommand_datas = []
    # 链接数据库获取清洗完成的岗位数据
    connect = pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="room",charset="utf8",cursorclass=pymysql.cursors.DictCursor)
    sql = "select  * from clean_rooms"
    cursor = connect.cursor()
    cursor.execute(sql)
    jobs = cursor.fetchall()
    connect.close()
    # 遍历所有的岗位信息，先把岗位向量化，然后和参数的向量化求余弦值（推荐算法的核心），判断余弦值>=0.8 加入推荐数组
    for job in jobs:
        # job向量化
        job_vec_array = room_vector.jobs_vec(job)
        # 将参数向量化数组和job向量化数组转成向量
        param_vec = np.array(param_array)
        job_vec = np.array(job_vec_array)
        # 两个向量的余弦值
        cos = np.dot(param_vec, job_vec)/(np.linalg.norm(param_vec)*np.linalg.norm(job_vec))
        # 判断余弦值是不是大于等于0.8
        if cos >= 0.9:
            job['job_score'] = cos*100
            recommand_datas.append(job)
    return recommand_datas