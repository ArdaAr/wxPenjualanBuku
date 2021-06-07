from database import db1

class buku():
    def __init__(self):
        self.id = None
        self.judul = None
        self.kategori = None
        self.harga = None
        self.penerbit = None
        self.stok = None
        self.gambar = None
    
    def stokNambah(self,jml):
        query = "UPDATE Buku SET Stok =%s WHERE ID_Buku=%s"
        self.stok += jml
        val = (self.stok,self.id)
        try:
            db1.cursor.execute(query,val)
            db1.conn.commit()
            print(self.stok)
        except:
            print("!!!!!!! Data Tidak Berhasil Dimasukkan !!!!!!!")
        return self.stok

    def stokBerkurang(self,qty):
        self.stok -= qty
        query = "UPDATE Buku SET stok = %s WHERE ID_Buku=%s"
        val = (self.stok, self.id)
        db1.cursor.execute(query,val)
        db1.conn.commit()
        return self.stok

    def getDataBuku(self,id):
        data = self.getByID(id)
        for i in data:
            self.id = i[0]
            self.judul = i[1]
            self.kategori = i[2]
            self.harga = i[3]
            self.penerbit = i[4]
            self.stok = i[5]
            self.gambar = i[6]
    
    def getStok(self,id):
        query = "Select stok from buku where id_buku=%s"
        val = (id,)
        stok = db1.cursor.execute(query,val)
        return stok
    
    def getByID(self,id):
        db1.getConn()
        sql = "Select * from buku where id_buku=%s"       
        val = (id,)
        db1.cursor.execute(sql,val)    
        all = db1.cursor.fetchall()
        return all

    def show(self, *argv):
        if len(argv)==0:
            buku = self.showAll()
        elif len(argv)==1:
            buku = self.showCategory(argv[0])
        else:
            buku = self.showHarga(argv[0],argv[1])
        return buku

    def showAll(self):
        db1.getConn()
        sql = "select * from buku"
        db1.cursor.execute(sql)
        return self.showData()
    
    def showCategory(self):
        kategori = input("Masukkan Kategori Buku : ")
        db1.getConn()
        sql = "Select * from Buku where kategori_buku=%s"       
        val = (kategori,)
        db1.cursor.execute(sql,val)    
        return self.showData()
        
    def showHarga(self):
        hargaMin = int(input("Masukkan Harga Minimal : "))
        hargaMax = int(input("Masukkan Harga Maksimal : "))
        db1.getConn()
        sql = "Select * from Buku where Harga between %s and %s"       
        val = (hargaMin,hargaMax)
        db1.cursor.execute(sql,val)
        return self.showData()

    def showData(self):
        all = db1.cursor.fetchall()    
        if len(all)>0:
            print("||","  "*2,"ID","  "*2,"||",end="")
            print("  "*2,"JUDUL BUKU","  "*2,"||",end="")
            print("  "*2,"KATEGORI","  "*2,"||",end="")
            print("  "*2,"HARGA","  "*2,"||",end="")
            print("  "*2,"PENERBIT","  "*2,"||",end="")
            print("  "*2,"STOK","  "*2,"||",end="")
            print()
            for i in all:
                print(" "*7,i[0], end=" "*4)
                print(" "*7,i[1], end=" "*4)
                print(" "*7,i[2], end=" "*4)
                print(" "*7,i[3], end=" "*4)
                print(" "*7,i[4], end=" "*4)
                print(" "*7,i[5], end=" "*4)
                print()
            return all
        else:
            print("Maaf Buku yang anda Cari tidak ada !")

# b1 = buku()
# b1.getDataBuku()
# print(b1.judul)
word = '123124/ewqe'
print(word[7:])