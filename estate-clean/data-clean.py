"""
租房信息清洗程序
"""
import pymysql
import re

# 连接数据库
connect = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="room",
                          cursorclass=pymysql.cursors.DictCursor, charset="utf8", autocommit=True)

# 查询数据库中标题、价格和面积不为空的数据
sql = "select * from rooms where job_title IS NOT NULL AND job_price IS NOT NULL AND job_area IS NOT NULL AND job_orientation IS NOT NULL"
cursor = connect.cursor()
cursor.execute(sql)
rentals = cursor.fetchall()

# 创建清洗后的表 clean_home，包含 UNIQUE(title, address) 约束，避免相同标题和地址的重复数据
sql = "create table if not exists  clean_rooms (job_title VARCHAR(255) NOT NULL,job_way VARCHAR(50),job_house VARCHAR(50),job_area VARCHAR(50),job_orientation VARCHAR(50),job_address VARCHAR(255),job_price VARCHAR(255),UNIQUE(job_title, job_address))"
cursor.execute(sql)

# 用于向清洗表中添加数据的SQL语句
sql = "insert into clean_rooms values (%(job_title)s, %(job_way)s, %(job_house)s, %(job_area)s, %(job_orientation)s, %(job_address)s, %(job_price)s)"

for rental in rentals:
    # 直接保留原始价格格式，不对 price 字段进行任何处理
    rental['job_price'] = rental['job_price']

    # 面积处理
    area_str = rental['job_area']
    area = float(re.sub(r"[^\d.]", "", area_str)) if area_str else 0.0
    rental['job_area'] = area

    # 户型处理
    house = rental['job_house']
    if not any(room in house for room in ['1室', '2室', '3室', '4室', '5室']):
        rental['job_house'] = '其他'

    # 插入清洗后的数据，使用 REPLACE INTO 避免重复
    try:
        cursor.execute(sql, rental)
    except pymysql.IntegrityError as e:
        print(f"重复数据跳过：{rental['job_title']} - {rental['job_address']}")
        continue  # 跳过当前循环，不插入数据

# 提交事务
connect.commit()

# 关闭数据库连接
cursor.close()
connect.close()
print("清洗完成")
