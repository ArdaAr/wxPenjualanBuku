from wx.core import CANCEL
from noname import menuAdmin,viewTambahBuku
from database import db1
from PIL import Image
from renderer import MyImageRenderer
import wx

class dashboardAdmin(menuAdmin):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initViewTambahBuku()
        # self.SetSize(self.parent.GetSize())
        # print(self.GetSize())
        self.setColumn()
        self.getListDataBuku()
        # self.showDataPesanan()
        # self.m_notebook1.Show()

    def goLogout(self,event):
        self.Hide()
        self.Refresh()
        self.parent.resetForm()

    def setColumn(self):
        # set column
        self.columnPesanan = ['Id Pesanan','Nama Customer','Nama Buku','Quantity','Tanggal','Total Harga']
        for idx,col in enumerate(self.columnPesanan):
            self.m_grid1.SetColLabelValue(idx,col)
        self.columnProduk = ['Gambar','Judul','Kategori','Harga','Stok','Penerbit','Opsi Edit', 'Opsi Delete']
        for idx,col in enumerate(self.columnProduk):
            self.dataProduk.SetColLabelValue(idx,col)
        self.dataProduk.HideRowLabels()

    def showDataPesanan(self):
        self.dataPesanan = self.getDataPesanan()
        for rowindex, row in enumerate(self.dataPesanan):
            self.m_grid1.AppendRows()
            self.m_grid1.SetRowSize(rowindex,50)
            for colIndex, col in enumerate(row):
                self.m_grid1.SetColSize(colIndex,100)
                self.m_grid1.SetCellValue(rowindex,colIndex,str(col))
        # self.m_grid1.AutoSize()

    def getDataPesanan(self):
        query = "SELECT id_pesanan,Nama_Customer,judul,quantity,DATE_FORMAT(tanggal,'%Y-%m-%d'),total_harga FROM pesanan p join customer c on p.id_customer=c.id_user join buku b on p.id_buku=b.id_buku"
        db1.cursor.execute(query)
        return db1.cursor.fetchall()

    def initViewTambahBuku(self):
        self.addStock = panelTambahBuku(self.parent)
        self.addStock.Hide()

    def goTambahStok(self, event):
        self.Hide()
        self.addStock.Show()

    def getDataProduk(self,listData):
        self.data = listData
        self.dataProduk.ClearGrid()
        if self.dataProduk.GetNumberRows() != 0:
            self.dataProduk.DeleteRows(numRows=self.dataProduk.GetNumberRows())
        for rowIndex, row in enumerate(self.data):
            self.dataProduk.AppendRows()
            self.dataProduk.SetRowSize(rowIndex,100)
            for columnIndex, col in enumerate(row):
                if columnIndex == 0:
                    self.dataProduk.SetColSize(columnIndex,100)
                    self.img = wx.Bitmap('pic/'+col, wx.BITMAP_TYPE_ANY)
                    self.image = MyImageRenderer(self.img)
                    self.dataProduk.SetCellRenderer(rowIndex,0,self.image)
                elif columnIndex == 6:
                    self.dataProduk.SetColSize(columnIndex,100)
                    self.dataProduk.SetCellValue(rowIndex,6,'EDIT')
                    self.dataProduk.SetCellBackgroundColour(rowIndex, 6, wx.Colour('blue'))
                    self.dataProduk.SetCellTextColour(rowIndex, 6, wx.Colour('white'))
                    continue
                elif columnIndex == 7:
                    self.dataProduk.SetColSize(columnIndex,100)
                    self.dataProduk.SetCellValue(rowIndex,7,'DELETE')
                    self.dataProduk.SetCellBackgroundColour(rowIndex, 7, wx.Colour('red'))
                    self.dataProduk.SetCellTextColour(rowIndex, 7, wx.Colour('white'))
                    continue
                self.dataProduk.SetColSize(columnIndex,200)
                self.dataProduk.SetCellValue(rowIndex,columnIndex,str(col))

    def getListDataBuku(self):
        sql = "select gambar,judul,kategori,harga,stok,penerbit,id_buku,k.id_kategori from buku b join kategori k on b.id_kategori=k.id_kategori"
        db1.cursor.execute(sql)
        all = db1.cursor.fetchall()
        # print(all)
        self.getDataProduk(all)
    
    def selectedCell(self, event):
        self.id = self.data[event.GetRow()][6]
        if event.GetCol() == 6:
            self.editBuku(event.GetRow())
        elif event.GetCol() == 7:
            # ok = 5100, cancel=5101
            dialog = wx.MessageDialog(self.parent, 'Anda Yakin akan menghapus buku ini?', style=CANCEL)
            dialogValue = dialog.ShowModal()
            if dialogValue == 5100:
                self.hapusBuku(self.id)

    def editBuku(self,row):
        dataForEdit = []
        for idx in range(self.dataProduk.GetNumberCols()):
            dataForEdit.append(self.dataProduk.GetCellValue(row,idx))
        self.addStock.goEdit(dataForEdit,self.id)
        self.addStock.Show()
        self.Hide()

    def hapusBuku(self,id):
        idBuku = id
        query = "DELETE FROM buku where id_buku=%s"
        val = (idBuku,)
        db1.cursor.execute(query,val)
        db1.conn.commit()
        self.getListDataBuku()

class panelTambahBuku(viewTambahBuku):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.comboVal = None
        self.edit = False
        self.SetSize(self.parent.GetSize())
        # self.m_comboBox4.Append("tess")
        self.setCombo()

    def goBack(self, event):
        self.Hide()
        self.parent.dbAdmin.Show()
        self.parent.dbAdmin.getListDataBuku()

    def goEdit(self,data,id):
        self.idEdit = id
        self.edit = True
        self.m_textCtrl9.SetValue(data[1])
        self.m_textCtrl11.SetValue(data[3])
        self.m_textCtrl12.SetValue(data[4])
        self.m_textCtrl13.SetValue(data[5])
        self.m_comboBox4.SetValue(data[2])

    def setValueCombo(self, event):
        if self.m_comboBox4.Value == 'Categories':
            self.comboVal = None
        else:
            query = "SELECT id_kategori from kategori where kategori=%s"
            val = (self.m_comboBox4.Value,)
            db1.cursor.execute(query,val)
            self.comboVal = db1.cursor.fetchone()[0]
        print(self.comboVal)

    def clearPath(self,path):
        indexSlash = 0
        for idx,alph in enumerate(path):
            if alph == "\\":
                indexSlash=idx
        return path[(indexSlash+1):]

    def saveImage(self, img, newPath):
        fd_img = open(img, 'wb')
        image = Image.open(fd_img)
        image.save(newPath, image.format)
        fd_img.close()

    def saveData(self, event):
        judul = self.m_textCtrl9.GetValue()
        harga = (self.m_textCtrl11.GetValue())
        stok = (self.m_textCtrl12.GetValue())
        penerbit = self.m_textCtrl13.GetValue()
        kategori = self.comboVal
        gambar = self.clearPath(self.m_filePicker2.GetPath())
        self.saveImage(self.m_filePicker2.GetPath(),gambar)
        print(judul,harga,stok,penerbit,kategori,gambar)
        if (judul and ( harga and (stok and (penerbit and (kategori and gambar))))):
            try:
                if (self.edit):
                    query = "update buku set judul=%s, id_kategori=%s, harga=%s, penerbit=%s, stok=%s, gambar=%s where id_buku = %s"
                    val = (judul,kategori,harga,penerbit,stok,gambar,self.idEdit)
                else:
                    query = "insert into buku(judul,id_kategori,harga,penerbit,stok,gambar) values(%s,%s,%s,%s,%s)"
                    val = (judul,kategori,harga,penerbit,stok,gambar)
                self.parent.database.cursor.execute(query,val)
                self.parent.database.conn.commit()
                self.parent.showDialog("Data Buku Berhasi Dimasukkan !")
                self.edit = False
            except:
                self.parent.showDialog("Data Buku Gagal Dimasukkan !")
        else:
            self.parent.showDialog("Data Harus Diisi !")

    def setCombo(self):
        query = "SELECT kategori from kategori"
        db1.cursor.execute(query)
        list = db1.cursor.fetchall()
        for item in list:
            self.m_comboBox4.Append(item[0])

    def onCombo(self, event):
        self.m_comboBox4.SetLabel("You selected"+self.combo.GetValue()+" from Combobox") 
