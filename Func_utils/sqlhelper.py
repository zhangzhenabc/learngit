import pymysql
from get_pro_absolute import host,user,passwd,port,db

class MySql(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host= host,
            user= user,
            passwd=passwd,
            port= int(port),
            db=db,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    def fetch_all(self, sql: str, args=None):
        try:
            self.cursor.execute(sql, args)
        except:
            self.conn.rollback()
        return self.cursor.fetchall()

    def fetch_one(self, sql: str, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()

    def execute(self, sql, args=None):
        self.rows = self.cursor.execute(sql, args)
        self.conn.commit()
        return self.rows

    def executemany(self, sql: str, data: list):
        self.rows = self.cursor.executemany(sql, data)
        self.conn.commit()
        return self.rows


class MySqlDic(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='139.155.7.36',
            user='qianroot',
            passwd='qian@125',
            port=3306,
            db='control',
            charset='utf8'
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    def fetch_all(self, sql: str, args=None):
        try:
            self.cursor.execute(sql, args)
        except:
            self.conn.rollback()
        return self.cursor.fetchall()

    def fetch_one(self, sql: str, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()

    def execute(self, sql, args=None):
        self.rows = self.cursor.execute(sql, args)
        self.conn.commit()
        return self.rows

    def executemany(self, sql: str, data: list):
        self.rows = self.cursor.executemany(sql, data)
        self.conn.commit()
        return self.rows