from noname import filterPrice

class comboFilterHarga(filterPrice):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def getDataFilter(self):
        self.min = self.hargaAwal.GetValue()
        self.max = self.hargaAkhir.GetValue()

    def okFilter(self, event):
        self.Close()