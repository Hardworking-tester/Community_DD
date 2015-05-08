#encoding_utf-8
import MySQLdb

class GetData():
    def getDataFromMysql(self):
        conn=MySQLdb.connect(host='192.168.1.88',user='root',passwd='password',db='app')
        cursor=conn.cursor()
        sql='select user.experience from user where phone=18638135380'
        cursor.execute(sql)
        # rs=cursor.fetchall()
        # for x in rs:
        #     print x
        rs=cursor.fetchone()
        conn.close()
        for i in rs:

            return i