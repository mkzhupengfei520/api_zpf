# import pymysql.cursors
# from os.path import abspath,dirname
# import configparser as cparser
# base_dir =  os.path.split(os.path.realpath(__file__))
# base_dir = base_dir.replace('\\', '/')
# file_path = base_dir + "/db_config.ini"
# print(file_path)
#
# #初始化
# cf = cparser.ConfigParser()
import os
import configparser
import pymysql

base_dir = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(base_dir, "db_config.ini")

conf = configparser.ConfigParser()
conf.read(configpath)

#读取配置文件
host = conf.get("mysql", "host")
port = conf.get("mysql", "port")
user = conf.get("mysql", "user")
password = conf.get("mysql", "password")
db =conf.get("mysql", "db_name")
print(host)

class DB:
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    def delete(self,table_name):
         real_sql1 = "delete a from  "+table_name + "  a ,(select  max(id) as max_id  from   "+table_name+" )b  where  a.id = b.max_id;"

         #cursor = self.connection.cursor()
         with self.connection.cursor() as cursor:

             cursor.execute(real_sql1)
             result = cursor.fetchall()
         self.connection.commit()

         # # try:
         #     # 执行SQL语句
         #     cursor.execute(real_sql1)
         #
         #     # 提交修改
         #     self.connection.commit()
         # except:
         #     print ('删除数据失败!')
         #     # 发生错误时回滚
         #     self.connection.rollback()



    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:

            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


    def select(self,table_name):
        real_sql = "select * from "+table_name+" where id = (select max(id) from "+table_name+")"
        print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            result = cursor.fetchall()
        self.connection.commit()
        print(result[0]['id'])




if __name__ == '__main__':
    db = DB()
    table_name = "sms_send_log"
    data = {'id': 305, 'user_id': 13516171, 'mobile': '15549430719', 'biz_type': 0, 'buss_type': 0,
            'content': '【食享会】短信验证码： 2711 ，此验证码10分钟内有效，为保障用户安全，请勿将验证码泄露给他人。', 'send_flag': 1,'remark':'',
            'creator':13516171,'creator_name':'wode','create_time':'2020-05-16 15:17:57','creator_ip':'','modifier':13516171, 'modifier_name':'wode',
            'modify_time':'2020-05-16 15:17:57','modifier_ip':'','delete_flag':'ture'}
    table_name2 = "user_info"
    data2 = {'realname': 'alen', 'phone': 12312341234, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1}

    #db.clear(table_name)
    #db.insert(table_name, data)
    #db.select(table_name)
    db.delete(table_name)
    db.close()




