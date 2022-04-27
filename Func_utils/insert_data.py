# -*- coding: utf-8 -*-
from Func_utils.sqlhelper import MySql


class insert_data:
    def __init__(self):
        self.mysql = MySql()

    def insert_user_sql(self, records):
        print(records[0])
        sql = f"""
        INSERT INTO `user` ( id, `name`, password, is_in_school,student_id,school_id,`role`,`state`) 
        VALUES ('{records[0]}','{records[1]}','{records[2]}','{records[3]}','{records[4]}','{records[5]}','{records[6]}','{records[7]}')
        """

        res = self.mysql.execute(sql)
        print('res====', res)
        return res


if __name__ == '__main__':


    record = [1120, '1234', '1', 1, 1, 1, 'A','A']



    res=insert_data().insert_user_sql(record)
    print('res======',res)
