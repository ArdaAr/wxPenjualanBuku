from noname import viewCart
from database import db1

class cartView(viewCart):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.SetSize(self.parent.GetSize())
        self.cart = self.parent.cart
        self.buyClicked = False
        # data pesanan -> [idbuku, judul, harga, stok, quantity, total] which is len=5
        self.dataPesanan = []
        self.getDataCart()
        self.initColumn()
        self.showIdentity()

    def getDataCart(self):
        for idx,row in enumerate(self.cart):
            id = row[0]
            query = "SELECT id_buku,judul,harga,stok from buku where id_buku=%s"
            val = (id,)
            db1.cursor.execute(query,val)
            data = db1.cursor.fetchall()[0]
            jmlHarga = data[2]*row[1]
            self.dataPesanan.append([i for i in (data)])
            self.dataPesanan[idx].append(row[1])
            self.dataPesanan[idx].append(jmlHarga)
        print(self.dataPesanan)

    def showDataPesanan(self):
        self.jmlHarga = 0
        for rowIndex, row in enumerate(self.dataPesanan):
            self.m_grid3.AppendRows()
            self.m_grid3.SetRowSize(rowIndex,50)
            for colIndex, col in enumerate(row[1:]):
                print(colIndex)
                self.m_grid3.SetColSize(colIndex,85)
                self.m_grid3.SetCellValue(rowIndex,colIndex,str(col))
                if colIndex==4:
                    self.m_grid3.SetCellValue(rowIndex,4,str(col))
                    self.jmlHarga += col
        # self.m_grid3.AutoSize()

    def showIdentity(self):
        self.showDataPesanan()
        self.nama.SetLabel(self.parent.dataUser.nama)
        self.telp.SetLabel(self.parent.dataUser.noHp)
        self.alamat.SetLabel(self.parent.dataUser.alamat)
        self.totalHarga.SetLabel(str(self.jmlHarga))
        print(self.jmlHarga)
    
    def initColumn(self):
        self.m_grid3.SetColLabelValue(0,'Judul')
        self.m_grid3.SetColLabelValue(3,'Quantity')
        self.m_grid3.SetColLabelValue(1,'Harga')
        self.m_grid3.SetColLabelValue(4,'Jumlah Harga')
        self.m_grid3.SetColLabelValue(2,'Stok')
        # self.m_grid3.SetSize(self.parent.GetSize())

    def goBack(self, event):
        data = self.parent.dashboard.getListDataBuku()
        self.parent.dashboard.showData(data)
        self.parent.dashboard.Show()
        self.Hide()

    def updateStok(self,id,newStok):
        query ="Update buku set stok=%s where id_buku=%s"
        id_Buku = id
        stokBaru = newStok
        val = (stokBaru,id_Buku)
        db1.cursor.execute(query,val)
        db1.conn.commit()

    def goBuy(self, event):
        self.buyClicked = True
        try:
            for rowIndex, row in enumerate(self.dataPesanan): 
                query = "INSERT INTO pesanan(id_customer,id_buku,quantity,total_harga) values(%s,%s,%s,%s)"
                idCst = self.parent.dataUser.id
                idbuku = row[0]
                qty = row[4]
                newstok = row[3]-qty
                val = (idCst,idbuku,qty,self.jmlHarga)
                db1.cursor.execute(query,val)
                db1.conn.commit()
                self.updateStok(idbuku,newstok)
                self.parent.showDialog("Berhasil Dibeli")
                self.parent.cart = []
        except:
            self.parent.showDialog("Gagal Dibeli")
            self.buyClicked = False