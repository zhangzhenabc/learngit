# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 16:28
# @Author  : zhangzhen
# @Email   : 858476928@qq.com
# @File    : delet_data.py
# @Software: PyCharm
from Func_utils.sqlhelper import MySql


class delete_sql:
    def __init__(self):
        self.mysql = MySql()

    def delete_user_sql(self, record):
        sql = f'''
               delete from `user` where id='{record[0]}'
           '''
        # print(sql)
        res = self.mysql.execute(sql)
        return res
