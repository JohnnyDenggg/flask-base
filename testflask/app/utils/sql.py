import pymysql

def db_conn(sql,*args):

    conn = pymysql.connect(host="deng.synology.me", user ="root", password ="Shanghai1!", database ="un1q", charset ="utf8",cursorclass=pymysql.cursors.DictCursor)
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql,*args)
        data = cursor.fetchall()
        conn.commit()
        if not data:
            data = cursor.rowcount
    except:
        data = False
        conn.rollback()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()
    return data