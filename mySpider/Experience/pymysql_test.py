import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='work')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询，获取数据库版本
cursor.execute("select version()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()

print(data)

# 关闭不使用的游标对象
cursor.close()
# 关闭数据库连接
db.close()
