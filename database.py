import mysql.connector
from mysql.connector.cursor import SQL_COMMENT

class dbConnection():
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
    
    def getConn(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print('Gagal connect dengan database {}'.format(e))
            
db1 = dbConnection("localhost","root","","jual_buku")
db1.getConn()
# sql = "select gambar,judul,kategori,harga,stok,penerbit,id_buku from buku b join kategori k on b.id_kategori=k.id_kategori"
# db1.cursor.execute(sql)
# all = db1.cursor.fetchall()
# print(all)