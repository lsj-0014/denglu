import pymysql

# 连接数据库
connect = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='room', charset='utf8',
                          cursorclass=pymysql.cursors.DictCursor, autocommit=True)


# 统计不同户型的数量
def house_statistics(connect):
    cursor = connect.cursor()
    # 创建存储统计数据的表
    sql = '''CREATE TABLE IF NOT EXISTS house_statistics(job_house VARCHAR(255), house_count INT)'''
    cursor.execute(sql)
    # 清空表中的数据
    sql = '''DELETE FROM house_statistics'''
    cursor.execute(sql)
    # 创建存储统计数据的表
    sql = '''
    INSERT INTO house_statistics 
select *,count(*) from (SELECT CASE
            WHEN job_house LIKE '4室2厅%' THEN '4室2厅'
            WHEN job_house LIKE '3室1厅%' THEN '3室1厅'
            WHEN job_house LIKE '3室2厅%' THEN '3室2厅'
            WHEN job_house LIKE '2室1厅%' THEN '2室1厅'
            WHEN job_house LIKE '2室2厅%' THEN '2室2厅'
            ELSE '其他'
            END AS job_house
    FROM clean_rooms) as house_statistics group by house_statistics.job_house
    '''
    cursor.execute(sql)
    connect.commit()

# 统计不同面积区间的数量
def area_statistics(connect):
    cursor = connect.cursor()
    # 创建存储统计数据的表
    sql = '''CREATE TABLE IF NOT EXISTS area_statistics(job_area VARCHAR(255), area_count INT)'''
    cursor.execute(sql)
    # 清空表中的数据
    sql = '''DELETE FROM area_statistics'''
    cursor.execute(sql)
    # 统计不同面积区间的数量
    sql = '''
    INSERT INTO area_statistics
select *,count(*) from (SELECT CASE
            WHEN FLOOR(job_area) <= 50 THEN '0-50'
            WHEN FLOOR(job_area) BETWEEN 51 AND 99 THEN '51-100'
            WHEN FLOOR(job_area) BETWEEN 101 AND 149 THEN '101-150'
            WHEN FLOOR(job_area) BETWEEN 150 AND 199 THEN '151-200'
            ELSE '200以上'
            END AS job_area
FROM clean_rooms) as area_statistics group by area_statistics.job_area
    '''
    cursor.execute(sql)

def price_statistics(connect):
    cursor = connect.cursor()
    # 创建存储统计数据的表
    sql = '''CREATE TABLE IF NOT EXISTS price_statistics(job_price VARCHAR(255), price_count INT)'''
    cursor.execute(sql)
    # 清空表中的数据
    sql = '''DELETE FROM price_statistics'''
    cursor.execute(sql)
    # 统计不同面积区间的数量
    sql = '''
    INSERT INTO price_statistics
select *,count(*) from (SELECT CASE
            WHEN FLOOR(job_price) <= 2000 THEN '0-2000'
            WHEN FLOOR(job_price) BETWEEN 2001 AND 5000 THEN '2001-5000'
            WHEN FLOOR(job_price) BETWEEN 5001 AND 10000 THEN '5001-10000'
            WHEN FLOOR(job_price) BETWEEN 10001 AND 20000 THEN '10001-20000'
            ELSE '20000以上'
            END AS job_price
FROM clean_rooms) as price_statistics group by price_statistics.job_price
    '''
    cursor.execute(sql)

# 统计房屋朝向的数量
def orientation_statistics(connect):
    cursor = connect.cursor()
    # 创建存储统计数据的表
    sql = '''CREATE TABLE IF NOT EXISTS orientation_statistics(job_orientation VARCHAR(255), orientation_count INT)'''
    cursor.execute(sql)
    # 清空表中的数据
    sql = '''DELETE FROM orientation_statistics'''
    cursor.execute(sql)
    # 统计不同朝向的房屋数量
    sql = '''
    INSERT INTO orientation_statistics
    SELECT job_orientation, COUNT(*) AS orientation_count
    FROM clean_rooms
    GROUP BY job_orientation
    '''
    cursor.execute(sql)

# 统计房屋方式的数量
def way_statistics(connect):
    cursor = connect.cursor()
    # 创建存储统计数据的表
    sql = '''CREATE TABLE IF NOT EXISTS way_statistics(job_way VARCHAR(255), way_count INT)'''
    cursor.execute(sql)
    # 清空表中的数据
    sql = '''DELETE FROM way_statistics'''
    cursor.execute(sql)
    # 统计不同朝向的房屋数量
    sql = '''
    INSERT INTO way_statistics
    SELECT job_way, COUNT(*) AS way_count
    FROM clean_rooms
    GROUP BY job_way
    '''
    cursor.execute(sql)

# 调用函数进行统计
house_statistics(connect)
area_statistics(connect)
orientation_statistics(connect)
price_statistics(connect)
way_statistics(connect)

print("房屋统计分析完成")