'''
研发一个推荐算法
    1、把清洗之后工作岗位给向量化，向量的维度代表岗位的角度
        [1 3 3]
        岗位的工作区域:
                其他  0
                东城区 1
                西城区 2
                ....朝阳区、丰台区、石景山区、海淀区、‌门头沟区、‌房山区、‌通州区、‌顺义区、‌昌平区、‌大兴区、‌怀柔区、平谷区、‌密云区、延庆区
        租金：
            (0-2000]  1
            (2000-5000]   2
            (5000-10000]   3
            (10000-2000]     4
            20000以上    5
        面积：
            (0-50]  1
            (50-100]   2
            (100-150]   3
            (150-200]     4
            200以上    5
        户型：
            其他   0
            2室1厅  1
            2室2厅   2
            3室1厅   3
            3室2厅   4
            4室2厅  5
        合租方式：
            整租   1
            合租主卧   2
            合租次卧   3
            合租单间  4
2、输入参数，参数向量化
3、计算参数向量化和岗位向量化的一个余弦值，0.85
'''


# 链接数据库 查询clean_jobs表中所有岗位数据，并且岗位数据转成向量
def jobs_vec(job):
    job_array = []
    # 先拿到岗位的五个信息
    job_address = job['job_address']
    job_price = job['job_price']
    job_house = job['job_house']
    job_way = job['job_way']
    # 类型转向量
    address_vec(job_address, job_array)
    price_to_vec(int(job_price), job_array)
    house_vec(job_house, job_array)
    way_vec(job_way, job_array)
    return job_array


def address_vec(job_address, job_array):
    if "东城" in job_address:
        job_array.append(1)
    elif "西城" in job_address:
        job_array.append(2)
    elif "朝阳" in job_address:
        job_array.append(3)
    elif "丰台" in job_address:
        job_array.append(4)
    elif "石景山" in job_address:
        job_array.append(5)
    elif "海淀" in job_address:
        job_array.append(6)
    elif "‌门头沟" in job_address:
        job_array.append(7)
    elif "‌房山" in job_address:
        job_array.append(8)
    elif "‌通州" in job_address:
        job_array.append(9)
    elif "‌顺义" in job_address:
        job_array.append(10)
    elif "‌昌平" in job_address:
        job_array.append(11)
    elif "‌大兴区" in job_address:
        job_array.append(12)
    elif "‌怀柔区" in job_address:
        job_array.append(13)
    elif "平谷区" in job_address:
        job_array.append(14)
    elif "‌密云区" in job_address:
        job_array.append(15)
    elif "延庆区" in job_address:
        job_array.append(16)
    else:
        job_array.append(0)
def price_to_vec(job_price, job_array):
    if job_price <= 2000:
        job_array.append(1)
    elif job_price <= 5000:
        job_array.append(2)
    elif job_price <= 10000:
        job_array.append(3)
    elif job_price <= 20000:
        job_array.append(4)
    else:
        job_array.append(5)
def area_to_vec(job_area, job_array):
    if job_area <= 50:
        job_array.append(1)
    elif job_area <= 100:
        job_array.append(2)
    elif job_area <= 150:
        job_array.append(3)
    elif job_area <= 200:
        job_array.append(4)
    else:
        job_array.append(5)
def house_vec(job_house, job_array):
    if job_house == "其他":
        job_array.append(0)
    elif job_house == "2室1厅":
        job_array.append(1)
    elif job_house == "2室2厅":
        job_array.append(2)
    elif job_house == "3室1厅":
        job_array.append(3)
    elif job_house == "3室2厅":
        job_array.append(4)
    else:
        job_array.append(5)
    return job_array
def way_vec(job_way, job_array):
    if job_way == "整租":
        job_array.append(1)
    elif job_way == "合租主卧":
        job_array.append(2)
    elif job_way == "合租次卧":
        job_array.append(3)
    else:
        job_array.append(4)
    return job_array

