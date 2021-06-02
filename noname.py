# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

username = 1000
password = 1001

###########################################################################
## Class form_login
###########################################################################

class form_login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tugas PBO", pos = wx.DefaultPosition, size = wx.Size( 688,515 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.loginPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self.loginPanel, wx.ID_ANY, u"Selamat Datang di Buku.in", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer13.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText11 = wx.StaticText( self.loginPanel, wx.ID_ANY, u"Silakan login untuk melanjutkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer13.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline3 = wx.StaticLine( self.loginPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer13.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self.loginPanel, wx.ID_ANY, wx.Bitmap( u"pic/durs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		bSizer13.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.SetMinSize( wx.Size( -1,0 ) )
		self.m_staticText1 = wx.StaticText( self.loginPanel, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 10 )

		self.input_username = wx.TextCtrl( self.loginPanel, username, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.input_username.SetMinSize( wx.Size( 200,35 ) )

		fgSizer2.Add( self.input_username, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.loginPanel, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 10 )

		self.input_password = wx.TextCtrl( self.loginPanel, password, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.input_password.SetMinSize( wx.Size( 200,35 ) )

		fgSizer2.Add( self.input_password, 0, wx.ALL, 5 )


		bSizer13.Add( fgSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 0 )

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		self.Login = wx.Button( self.loginPanel, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.Login, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.checkCustomer = wx.CheckBox( self.loginPanel, wx.ID_ANY, u"Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.checkCustomer, 0, wx.ALL, 5 )

		self.checkAdmin = wx.CheckBox( self.loginPanel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.checkAdmin, 0, wx.ALL, 5 )


		bSizer151.Add( bSizer16, 1, wx.ALIGN_CENTER, 5 )


		bSizer13.Add( bSizer151, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.m_staticline5 = wx.StaticLine( self.loginPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer13.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self.loginPanel, wx.ID_ANY, u"Belum memiliki akun?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer17.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self.loginPanel, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )

		bSizer17.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer13.Add( bSizer17, 1, wx.ALIGN_CENTER, 5 )


		self.loginPanel.SetSizer( bSizer13 )
		self.loginPanel.Layout()
		bSizer13.Fit( self.loginPanel )
		bSizer15.Add( self.loginPanel, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.kill )
		self.Bind( wx.EVT_SIZE, self.sizing )
		self.Login.Bind( wx.EVT_BUTTON, self.doLogin )
		self.checkCustomer.Bind( wx.EVT_CHECKBOX, self.isCustomer )
		self.checkAdmin.Bind( wx.EVT_CHECKBOX, self.isAdmin )
		self.m_button3.Bind( wx.EVT_BUTTON, self.goRegister )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def kill( self, event ):
		event.Skip()

	def sizing( self, event ):
		event.Skip()

	def doLogin( self, event ):
		event.Skip()

	def isCustomer( self, event ):
		event.Skip()

	def isAdmin( self, event ):
		event.Skip()

	def goRegister( self, event ):
		event.Skip()


###########################################################################
## Class dashboardPanel
###########################################################################

class dashboardPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 672,475 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer15.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"My Account", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer17.Add( bSizer15, 0, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"All Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer13.Add( self.m_button12, 0, wx.ALL, 5 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"By Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer13.Add( self.m_button13, 0, wx.ALL, 5 )

		m_comboBox2Choices = [ u"Categories" ]
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		self.m_comboBox2.SetSelection( 0 )
		bSizer13.Add( self.m_comboBox2, 0, wx.ALL, 8 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer13.Add( self.m_staticText51, 0, wx.ALL, 10 )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Checkout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer13.Add( self.m_button17, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.dataBuku = wx.grid.Grid( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,348 ), 0 )

		# Grid
		self.dataBuku.CreateGrid( 0, 7 )
		self.dataBuku.EnableEditing( False )
		self.dataBuku.EnableGridLines( False )
		self.dataBuku.EnableDragGridSize( False )
		self.dataBuku.SetMargins( 1, 1 )

		# Columns
		self.dataBuku.EnableDragColMove( False )
		self.dataBuku.EnableDragColSize( True )
		self.dataBuku.SetColLabelSize( 30 )
		self.dataBuku.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataBuku.EnableDragRowSize( True )
		self.dataBuku.SetRowLabelSize( 80 )
		self.dataBuku.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.dataBuku.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.dataBuku.SetLabelFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.dataBuku.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		# Cell Defaults
		self.dataBuku.SetDefaultCellFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Montserrat" ) )
		self.dataBuku.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		self.dataBuku.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.dataBuku.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer32.Add( self.dataBuku, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel8.SetSizer( bSizer32 )
		self.m_panel8.Layout()
		bSizer32.Fit( self.m_panel8 )
		bSizer17.Add( self.m_panel8, 1, wx.ALL|wx.EXPAND, 5 )

		self.logout = wx.Button( self, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.logout.SetBitmap( wx.NullBitmap )
		bSizer17.Add( self.logout, 0, wx.ALL, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.viewAccount )
		self.m_button12.Bind( wx.EVT_BUTTON, self.showAll )
		self.m_button13.Bind( wx.EVT_BUTTON, self.showByPrice )
		self.m_comboBox2.Bind( wx.EVT_COMBOBOX, self.setValueCombo )
		self.m_button17.Bind( wx.EVT_BUTTON, self.doCheckout )
		self.dataBuku.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.getCell )
		self.logout.Bind( wx.EVT_BUTTON, self.goLogout )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def viewAccount( self, event ):
		event.Skip()

	def showAll( self, event ):
		event.Skip()

	def showByPrice( self, event ):
		event.Skip()

	def setValueCombo( self, event ):
		event.Skip()

	def doCheckout( self, event ):
		event.Skip()

	def getCell( self, event ):
		event.Skip()

	def goLogout( self, event ):
		event.Skip()


###########################################################################
## Class addCartDialog
###########################################################################

class addCartDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Cart", pos = wx.DefaultPosition, size = wx.Size( 394,176 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( 1000,-1 ), 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer25.Add( self.m_staticText38, 0, wx.ALL, 5 )


		bSizer24.Add( bSizer25, 0, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Jumlah ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer26.Add( self.m_staticText39, 0, wx.ALL, 10 )

		self.quantityBeli = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0.000000, 1 )
		self.quantityBeli.SetDigits( 0 )
		bSizer26.Add( self.quantityBeli, 0, wx.ALL, 5 )


		bSizer24.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer28.Add( m_sdbSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer24.Add( bSizer28, 1, 0, 5 )


		self.SetSizer( bSizer24 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.addCartOk )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def addCartOk( self, event ):
		event.Skip()


###########################################################################
## Class filterPrice
###########################################################################

class filterPrice ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 394,202 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Filter Produk Berdasarkan Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		self.m_staticText48.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer29.Add( self.m_staticText48, 0, wx.ALL, 5 )

		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer29.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Batas Bawah Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		fgSizer5.Add( self.m_staticText50, 0, wx.ALL, 5 )

		self.hargaAwal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.hargaAwal, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Batas Atas Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer5.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.hargaAkhir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.hargaAkhir, 0, wx.ALL, 5 )


		bSizer29.Add( fgSizer5, 1, wx.EXPAND, 5 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		bSizer29.Add( m_sdbSizer2, 1, 0, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.okFilter )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def okFilter( self, event ):
		event.Skip()


###########################################################################
## Class registerPanel
###########################################################################

class registerPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 672,475 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Register Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer12.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Isi data kamu disini", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		self.m_staticText24.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer12.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText18 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer9.Add( self.m_staticText18, 0, wx.ALL, 8 )

		self.m_staticText19 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer9.Add( self.m_staticText19, 0, wx.ALL, 10 )

		self.m_staticText20 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer9.Add( self.m_staticText20, 0, wx.ALL, 10 )

		self.m_staticText21 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer9.Add( self.m_staticText21, 0, wx.ALL, 10 )

		self.m_staticText22 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer9.Add( self.m_staticText22, 0, wx.ALL, 10 )

		self.m_staticText23 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer9.Add( self.m_staticText23, 0, wx.ALL, 10 )

		self.m_staticText28 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Foto Profil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer9.Add( self.m_staticText28, 0, wx.ALL, 10 )


		bSizer13.Add( bSizer9, 0, 0, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl11 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl11, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl12, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl13, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl15, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.m_textCtrl8.SetMaxLength( 8 )
		bSizer10.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )

		self.imagePicker = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer10.Add( self.imagePicker, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer10, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button10 = wx.Button( self.m_panel2, wx.ID_ANY, u"REGISTER", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button10.SetBitmap( wx.NullBitmap )
		self.m_button10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "LEMON MILK Bold" ) )

		bSizer14.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button12 = wx.Button( self.m_panel2, wx.ID_ANY, u"KEMBALI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "LEMON MILK" ) )

		bSizer14.Add( self.m_button12, 0, wx.ALL, 5 )


		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer12 )
		self.m_panel2.Layout()
		bSizer12.Fit( self.m_panel2 )
		bSizer7.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.sizing )
		self.m_button10.Bind( wx.EVT_BUTTON, self.register )
		self.m_button12.Bind( wx.EVT_BUTTON, self.goBack )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def sizing( self, event ):
		event.Skip()

	def register( self, event ):
		event.Skip()

	def goBack( self, event ):
		event.Skip()


###########################################################################
## Class viewInfoAkun
###########################################################################

class viewInfoAkun ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 672,475 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"My Account", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer17.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Back", wx.Point( -1,-1 ), wx.DefaultSize, 0 )

		self.m_button12.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_OTHER ) )
		bSizer17.Add( self.m_button12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer15.Add( bSizer17, 0, wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer15.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		bSizer15.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.panelInfo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText17 = wx.StaticText( self.panelInfo, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer2.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.infoNama = wx.StaticText( self.panelInfo, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infoNama.Wrap( -1 )

		fgSizer2.Add( self.infoNama, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.panelInfo, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer2.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.infoAlamat = wx.StaticText( self.panelInfo, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infoAlamat.Wrap( -1 )

		fgSizer2.Add( self.infoAlamat, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.panelInfo, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		fgSizer2.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.infoEmail = wx.StaticText( self.panelInfo, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infoEmail.Wrap( -1 )

		fgSizer2.Add( self.infoEmail, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.panelInfo, wx.ID_ANY, u"Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer2.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.infoTelp = wx.StaticText( self.panelInfo, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infoTelp.Wrap( -1 )

		fgSizer2.Add( self.infoTelp, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.panelInfo, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer2.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.infoUsername = wx.StaticText( self.panelInfo, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infoUsername.Wrap( -1 )

		fgSizer2.Add( self.infoUsername, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self.panelInfo, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer2.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.infoPw = wx.StaticText( self.panelInfo, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infoPw.Wrap( -1 )

		fgSizer2.Add( self.infoPw, 0, wx.ALL, 5 )


		self.panelInfo.SetSizer( fgSizer2 )
		self.panelInfo.Layout()
		fgSizer2.Fit( self.panelInfo )
		bSizer15.Add( self.panelInfo, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.sizing )
		self.m_button12.Bind( wx.EVT_BUTTON, self.goBack )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def sizing( self, event ):
		event.Skip()

	def goBack( self, event ):
		event.Skip()


###########################################################################
## Class menuAdmin
###########################################################################

class menuAdmin ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 672,475 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Admin Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer31.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"LOGOUT", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button14.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_OTHER ) )
		self.m_button14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer31.Add( self.m_button14, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer31, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_panel7 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,200 ), wx.TAB_TRAVERSAL )
		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.dataProduk = wx.grid.Grid( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,500 ), 0 )

		# Grid
		self.dataProduk.CreateGrid( 0, 8 )
		self.dataProduk.EnableEditing( False )
		self.dataProduk.EnableGridLines( False )
		self.dataProduk.EnableDragGridSize( False )
		self.dataProduk.SetMargins( 0, 0 )

		# Columns
		self.dataProduk.EnableDragColMove( False )
		self.dataProduk.EnableDragColSize( True )
		self.dataProduk.SetColLabelSize( 30 )
		self.dataProduk.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataProduk.EnableDragRowSize( True )
		self.dataProduk.SetRowLabelSize( 80 )
		self.dataProduk.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.dataProduk.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.dataProduk.SetLabelFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.dataProduk.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		# Cell Defaults
		self.dataProduk.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer30.Add( self.dataProduk, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer30 )
		self.m_panel7.Layout()
		self.m_notebook1.AddPage( self.m_panel7, u"Data Produk", True )
		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.Size( 610,400 ), 0 )

		# Grid
		self.m_grid1.CreateGrid( 0, 6 )
		self.m_grid1.EnableEditing( False )
		self.m_grid1.EnableGridLines( False )
		self.m_grid1.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.AutoSizeRows()
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid1.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_grid1.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		# Cell Defaults
		self.m_grid1.SetDefaultCellTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer18.Add( self.m_grid1, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer18 )
		self.m_panel4.Layout()
		bSizer18.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"Lihat Pesanan", False )

		bSizer17.Add( self.m_notebook1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Tambah Stok", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button13.SetBitmap( wx.NullBitmap )
		self.m_button13.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer17.Add( self.m_button13, 0, wx.ALL|wx.SHAPED, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		# Connect Events
		self.m_button14.Bind( wx.EVT_BUTTON, self.goLogout )
		self.dataProduk.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectedCell )
		self.m_button13.Bind( wx.EVT_BUTTON, self.goTambahStok )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def goLogout( self, event ):
		event.Skip()

	def selectedCell( self, event ):
		event.Skip()

	def goTambahStok( self, event ):
		event.Skip()


###########################################################################
## Class viewTambahBuku
###########################################################################

class viewTambahBuku ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 672,475 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText30 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Form Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer20.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_staticline8 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer20.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		fgSizer3.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer3.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer3.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Penerbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		fgSizer3.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Kategori", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		fgSizer3.Add( self.m_staticText32, 0, wx.ALL, 5 )

		m_comboBox4Choices = [ u"Categories" ]
		self.m_comboBox4 = wx.ComboBox( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices, 0 )
		self.m_comboBox4.SetSelection( 0 )
		fgSizer3.Add( self.m_comboBox4, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Gambar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		fgSizer3.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer3.Add( self.m_filePicker2, 0, wx.ALL, 5 )


		bSizer21.Add( fgSizer3, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button15 = wx.Button( self.m_panel5, wx.ID_ANY, u"SIMPAN", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button15.SetBitmap( wx.NullBitmap )
		self.m_button15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer22.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self.m_panel5, wx.ID_ANY, u"KEMBALI", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button16.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_OTHER ) )
		self.m_button16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer22.Add( self.m_button16, 0, wx.ALL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer20 )
		self.m_panel5.Layout()
		bSizer20.Fit( self.m_panel5 )
		bSizer19.Add( self.m_panel5, 1, wx.EXPAND|wx.ALL, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()

		# Connect Events
		self.m_comboBox4.Bind( wx.EVT_COMBOBOX, self.setValueCombo )
		self.m_button15.Bind( wx.EVT_BUTTON, self.saveData )
		self.m_button16.Bind( wx.EVT_BUTTON, self.goBack )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def setValueCombo( self, event ):
		event.Skip()

	def saveData( self, event ):
		event.Skip()

	def goBack( self, event ):
		event.Skip()


###########################################################################
## Class viewCart
###########################################################################

class viewCart ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 672,475 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"My Cart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		self.m_staticText40.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer30.Add( self.m_staticText40, 0, wx.ALL, 5 )

		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer30.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid3 = wx.grid.Grid( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.Size( 610,200 ), 0 )

		# Grid
		self.m_grid3.CreateGrid( 0, 6 )
		self.m_grid3.EnableEditing( False )
		self.m_grid3.EnableGridLines( False )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.SetColSize( 0, 80 )
		self.m_grid3.SetColSize( 1, 80 )
		self.m_grid3.SetColSize( 2, 80 )
		self.m_grid3.SetColSize( 3, 93 )
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid3.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_grid3.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer33.Add( self.m_grid3, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel9.SetSizer( bSizer33 )
		self.m_panel9.Layout()
		bSizer33.Fit( self.m_panel9 )
		bSizer30.Add( self.m_panel9, 0, wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText41 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama Penerima", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		fgSizer4.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.nama = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama.Wrap( -1 )

		fgSizer4.Add( self.nama, 0, wx.ALL, 5 )

		self.telepon = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.telepon.Wrap( -1 )

		fgSizer4.Add( self.telepon, 0, wx.ALL, 5 )

		self.telp = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.telp.Wrap( -1 )

		fgSizer4.Add( self.telp, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		fgSizer4.Add( self.m_staticText45, 0, wx.ALL, 5 )

		self.alamat = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alamat.Wrap( -1 )

		fgSizer4.Add( self.alamat, 0, wx.ALL, 5 )

		self.m_staticText47 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Total Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		fgSizer4.Add( self.m_staticText47, 0, wx.ALL, 5 )

		self.totalHarga = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.totalHarga.Wrap( -1 )

		fgSizer4.Add( self.totalHarga, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( fgSizer4 )
		self.m_panel6.Layout()
		fgSizer4.Fit( self.m_panel6 )
		bSizer30.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Beli Sekarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_button21, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer31, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer30 )
		self.Layout()

		# Connect Events
		self.m_button20.Bind( wx.EVT_BUTTON, self.goBuy )
		self.m_button21.Bind( wx.EVT_BUTTON, self.goBack )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def goBuy( self, event ):
		event.Skip()

	def goBack( self, event ):
		event.Skip()


