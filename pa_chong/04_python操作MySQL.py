"""
SQL常用数据类型：

int 普通大小的整数，4字节，当然整型的类型还有tinyint，smallint，bigint等等，保存的长度不同

float 单精度浮点数，4字节

double 双精度浮点数，8字节

decimal（m,d）也是浮点数 m表示数字总位数,d表示保留到小数点后d位，不足部分就添0，如果不设置m、d默认保存精度是整型

varchar(n) 可变字符类型

char(n) 固定长度字符类型. n为0~255之间的整数，固定长度为n，不足后面补全空格

date 日期 YYYY-MM-DD 1000-01-01~9999-12-3，3字节

time 时间 HH:MM:SS -838:59:59~838:59:59，3字节

datetime 日期时间 YYYY-MM-DD HH:MM:SS 1000-01-01 00:00:00~ 9999-12-31 23:59:59，8字节


"""
from pymysql import *

"""
方法	                        说明
close()	                    关闭游标
execute(query, args=None)	执行单条语句，传入需要执行的语句，是string类型；同时可以给查询传入参数，
                            参数可以是tuple、list或dict。执行完成后，会返回执行语句的影响行数。
fetchone()	                取一条数据
fetchmany(n)	            取多条数据
fetchall()	                取所有数据
"""


def main():
    # 创建connection连接
    conn = connect(host='localhost', port=3306, database='ey_clock', user='root',
                   password='root', charset='utf8')
    # 获取cursor对象
    cs1 = conn.cursor()
    # 执行sql语句
    # query = "insert into goods(id,name,price,num) values(%s,%s,%s,%s)"
    # cs1.execute(query, (4, '蒙牛酸奶', 13.9, 88))
    query = "SELECT * FROM user_list"
    res = cs1.execute(query)
    print(res)
    res2 = cs1.fetchall()
    print(res2)

    # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
    conn.commit()

    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()


main()



