# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 16:32
# @Author  : zhangzhen
# @Email   : 858476928@qq.com
# @File    : update_data.py
# @Software: PyCharm

from Func_utils.sqlhelper import MySql


class update_sql:
    def __init__(self):
        self.mysql = MySql()

    def update_user_sql(self, record):
        sql = f'''
               update `user` set `name`='{record[1]}',password='{record[2]}',is_in_school='{record[3]}',student_id='{record[4]}',school_id='{record[5]}',
               `role` ='{record[6]}',`state` ='{record[7]}'  where id='{record[0]}'
           '''
        res = self.mysql.execute(sql)
        return res

# UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
