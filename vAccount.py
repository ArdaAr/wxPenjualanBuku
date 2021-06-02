from noname import viewInfoAkun
import wx


class viewAkun(viewInfoAkun):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.SetSize(self.parent.GetSize())
        self.objCustomer = self.parent.dataUser
        print(self.objCustomer.foto)
        self.showDataAkun()
    
    def showDataAkun(self):
        self.m_bitmap1.SetBitmap(wx.Bitmap( u"pic/"+(self.objCustomer.foto), wx.BITMAP_TYPE_ANY ))
        self.infoNama.SetLabel(self.objCustomer.nama)
        self.infoAlamat.SetLabel(self.objCustomer.alamat)
        self.infoEmail.SetLabel(self.objCustomer.email)
        self.infoTelp.SetLabel(self.objCustomer.noHp)
        self.infoUsername.SetLabel(self.objCustomer.username)
        self.infoPw.SetLabel(self.objCustomer.getPassword())

    def goBack(self, event):
        self.Hide()
        self.parent.dashboard.Show()