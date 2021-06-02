from hargaFilter import comboFilterHarga
from cart import cartView
import wx
from wx.core import ALIGN_CENTER, ComboBox
import wx.dataview
import mysql
from noname import addCartDialog, form_login,dashboardPanel, registerPanel
from admin import dashboardAdmin
from database import db1
from person import user,admin
from vAccount import viewAkun
from renderer import MyImageRenderer
from buku import buku

app = wx.App()

class loginForm(form_login):
    def __init__(self, parent):
        super(loginForm, self).__init__(parent)
        self.dashboard = panelDashboard(parent=self)
        self.dashboard.Hide()
        self.database = db1
        self.dbAdmin = dashboardAdmin(parent=self)
        self.dbAdmin.Hide()
        self.reg = panelRegister(parent=self)
        self.reg.Hide()
        self.checklisted = True
        self.cart = []

    # get data user dari database
    def getDataUsername(self, event, uname):
        self.checklisted = True
        val = (uname,)
        if self.checkAdmin.IsChecked():
            query = "SELECT * FROM admin WHERE username=%s"
            db1.cursor.execute(query,val)
            usr = db1.cursor.fetchone()
            # buat objek dari model admin
            if usr:
                objUser = admin(usr[1],usr[2],usr[3])
                db1.conn.commit()
                return objUser
            else:
                return False
        elif self.checkCustomer.IsChecked():
            query = "SELECT * FROM CUSTOMER WHERE username=%s"
            db1.cursor.execute(query,val)
            usr = db1.cursor.fetchone()
            # buat objek dari model customer
            if usr:
                objUser = user(usr[1],usr[2],usr[3],usr[4],usr[5],usr[6],usr[7],usr[0])
                db1.conn.commit()
                # print(objUser.id)
                return objUser
            else:
                return False
        else:
            self.checklisted = False

    def isAdmin(self, event):
        self.checkCustomer.SetValue(False)
    
    def isCustomer(self, event):
        self.checkAdmin.SetValue(False)

    def handleDataInput(self,event):
        username = self.input_username.GetValue()
        if (username):
            self.dataUser = self.getDataUsername(event,username)
            if self.checklisted:          
                if (self.dataUser):
                    password = self.input_password.GetValue()
                    if (password):
                        if (self.dataUser.cekPassword(password)):
                            if self.checkCustomer.IsChecked():
                                self.loginPanel.Hide()
                                data = self.dashboard.getListDataBuku()
                                self.dashboard.showData(data)
                                self.dashboard.Show()
                            else:
                                self.loginPanel.Hide()
                                self.dbAdmin.Show()
                                self.dbAdmin.showDataPesanan()
                        else:
                            self.showDialog("Password yang anda input salah !")
                    else:
                        self.showDialog("Data Password Harus Diisi !")   
                else:
                    self.showDialog("Data Username Tidak Ditemukan !")
            else:
                self.showDialog("Harap checklist role anda !")
        else:
            self.showDialog("Data Username Harus Diisi !")

    def showDialog(self,message):
        dial = wx.MessageDialog(self, message, style=wx.OK|wx.STAY_ON_TOP|wx.CENTRE)
        dial.ShowModal()

    def goRegister(self, event):
        self.loginPanel.Hide()
        self.reg.Show()

    def doLogin(self, event):
        self.handleDataInput(event)
        return super().doLogin(event)

    def sizing(self,event):
        self.loginPanel.SetSize(self.GetSize())
        # self.dashboard.SetSize(self.GetSize())

    def resetForm(self):
        self.input_username.Clear()
        self.input_password.Clear()
        self.checkAdmin.SetValue(False)
        self.checkCustomer.SetValue(False)
        self.loginPanel.Show()

class panelDashboard(dashboardPanel):
    def __init__(self, parent):
        dashboardPanel.__init__(self,parent)
        self.parent = parent
        # self.SetSize(self.parent.GetSize())
        self.idChoosen = None
        self.data = []
        self.setColumn()
        self.setChoices()
        print(self.m_panel8.GetSize())
        # self.img = wx.Bitmap("pic/arda.jpg", wx.BITMAP_TYPE_ANY)
        # self.image = MyImageRenderer(self.img)
        # self.dataBuku.SetCellRenderer(0,0,self.image)
        # self.showData()
        # self.cart = []

    def getCell(self, event):
        if event.GetCol() == 6:
            self.idChoosen = self.data[event.GetRow()][6]
            self.initBuku(self.idChoosen)
            self.add = dialogAddCart(self.parent, self.objBuku)
            self.add.ShowModal()

    def initBuku(self,id):
        self.objBuku = buku()
        self.objBuku.getDataBuku(id)
        print(self.objBuku.judul)

    def doCheckout(self, event):
        self.dataCart = cartView(self.parent)
        self.dataCart.Show()
        self.Hide()

    def showAll(self, event):
        # self.dataBuku.DeleteRows(numRows=self.dataBuku.GetNumberRows())
        data = self.getListDataBuku()
        self.showData(data)

    def setChoices(self):
        query = "SELECT kategori from kategori"
        db1.cursor.execute(query)
        list = db1.cursor.fetchall()
        for item in list:
            self.m_comboBox2.Append(item[0])

    def setValueCombo(self, event):
        if self.m_comboBox2.Value == 'Categories':
            comboBoxValue = None
        else:
            # self.dataBuku.DeleteRows(numRows=self.dataBuku.GetNumberRows())
            query = "select gambar,judul,kategori,harga,stok,penerbit,id_buku from buku b join kategori k on b.id_kategori=k.id_kategori where k.kategori=%s"
            val = (self.m_comboBox2.Value,)
            db1.cursor.execute(query,val)
            dataAll = db1.cursor.fetchall()
            self.showData(dataAll)

    def showByPrice(self, event):
        self.filterHarga = comboFilterHarga(self.parent)
        self.filterHarga.ShowModal()
        self.filterHarga.getDataFilter()
        query = "select gambar,judul,kategori,harga,stok,penerbit,id_buku from buku b join kategori k on b.id_kategori=k.id_kategori where harga between %s and %s order by harga"
        val = (self.filterHarga.min,self.filterHarga.max)
        # self.dataBuku.DeleteRows(numRows=self.dataBuku.GetNumberRows())
        db1.cursor.execute(query,val)
        dataAll = db1.cursor.fetchall()
        self.showData(dataAll)

    def viewAccount(self, event):
        self.Hide()
        self.akun = viewAkun(self.parent)
        self.akun.Show()

    def setColumn(self):
        self.dataBuku.SetColLabelValue(0,'Gambar')
        self.dataBuku.SetColLabelValue(1,'Judul')
        self.dataBuku.SetColLabelValue(2,'Kategori')
        self.dataBuku.SetColLabelValue(3,'Harga')
        self.dataBuku.SetColLabelValue(4,'Stok')
        self.dataBuku.SetColLabelValue(5,'Penerbit')
        self.dataBuku.SetColLabelValue(6,'Opsi')
        self.dataBuku.HideRowLabels()
        self.dataBuku.EnableEditing(False)

    def getListDataBuku(self):
        sql = "select gambar,judul,kategori,harga,stok,penerbit,id_buku from buku b join kategori k on b.id_kategori=k.id_kategori"
        db1.cursor.execute(sql)
        all = db1.cursor.fetchall()
        return all

    def showData(self,listData):
        self.data = listData
        self.dataBuku.ClearGrid()
        if self.dataBuku.GetNumberRows() != 0:
            self.dataBuku.DeleteRows(numRows=self.dataBuku.GetNumberRows())
        for rowIndex, row in enumerate(self.data):
            self.dataBuku.AppendRows()
            self.dataBuku.SetRowSize(rowIndex,100)
            for columnIndex, col in enumerate(row):
                if columnIndex==7:
                    self.dataBuku.SetColSize(columnIndex,100)
                    continue
                elif columnIndex == 0:
                    self.dataBuku.SetColSize(columnIndex,100)
                    self.img = wx.Bitmap('pic/'+col, wx.BITMAP_TYPE_ANY)
                    self.image = MyImageRenderer(self.img)
                    self.dataBuku.SetCellRenderer(rowIndex,0,self.image)
                    continue
                self.dataBuku.SetColSize(columnIndex,200)
                self.dataBuku.SetCellValue(rowIndex,columnIndex,str(col))
                self.dataBuku.SetCellValue(rowIndex,6,'ADD CART')
                self.dataBuku.SetCellBackgroundColour(rowIndex, 6, wx.Colour('red'))
                self.dataBuku.SetCellTextColour(rowIndex, 6, wx.Colour('white'))
        self.m_staticText51.SetLabel('{} data ditampilkan'.format(self.dataBuku.GetNumberRows()))

    def goLogout(self,event):
        self.Hide()
        self.parent.resetForm()

class dialogAddCart(addCartDialog):
    def __init__(self, parent, buku):
        super().__init__(parent)
        self.parent = parent
        self.objBuku = buku
        self.qtyBuku = 0
        self.quantityBeli.SetMax(self.objBuku.stok)
        self.m_staticText38.SetLabel('Anda Akan Menambahkan buku {} kedalam cart'.format(self.objBuku.judul))

    def addCartOk(self, event):
        # add identity cart
        self.qtyBuku = int(self.quantityBeli.GetValue())
        self.parent.cart.append([self.objBuku.id, self.qtyBuku])
        print(self.parent.cart)
        self.Close()

class panelRegister(registerPanel):
    def __init__(self, parent):
        registerPanel.__init__(self,parent)
        self.parent = parent
        # self.SetSize(self.parent.GetSize())

    def goBack(self, event):
        self.Hide()
        self.parent.resetForm()
    
    def register(self, event):
        # textctrl 11-15
        nama = self.m_textCtrl11.GetValue()
        alamat = self.m_textCtrl12.GetValue()
        email = self.m_textCtrl13.GetValue()
        telp = self.m_textCtrl14.GetValue()
        username = self.m_textCtrl15.GetValue()
        passwd = self.m_textCtrl8.GetValue()
        try:
            sql = "INSERT INTO Customer(Nama_Customer,Alamat,email,telepon,username,password) VALUES(%s,%s,%s,%s,%s,%s)"
            val = (nama,alamat,email,telp,username,passwd)
            db1.cursor.execute(sql,val)
            db1.conn.commit()
            self.parent.showDialog("Registrasi Berhasil")
            self.Hide()
            self.parent.resetForm()
        except mysql.connector.Error as e:
            print(e)
            self.parent.showDialog("Registrasi gagal")

formLogin1 = loginForm(parent=None)
formLogin1.Show()
app.MainLoop()