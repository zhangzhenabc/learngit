# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 19:55
# @Author  : zhangzhen
# @Email   : 858476928@qq.com
# @File    : search_data.py
# @Software: PyCharm

from Func_utils.sqlhelper import MySql

class search_data:
    def __init__(self):
        self.mysql = MySql()

    def search_user_sql(self, records):
        print(records)
        sql = f'''
              select `name` , password, is_in_school,student_id,school_id,`role`,`state`
              from `user` where id='{records[0]}'
              '''
        res = self.mysql.fetch_all(sql)
        print('res',type(res))
        return res
if __name__ == '__main__':
    records=[120,'x']
    res = search_data().search_user_sql(records)
    print('res======', res)