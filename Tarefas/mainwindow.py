import wx

class MW(wx.Frame):

	def __init__(self, *argv, **kw):
		super(MW, self).__init__(*argv,**kw)

		self.Pack()

	def Pack(self):
		self.pnl = wx.Panel(self)
		self.l1 = wx.StaticText(self.pnl,label="Tarefa:")
		self.l2 = wx.StaticText(self.pnl,label="Pendentes:")
		#self.l3 = wx.Label(self.pnl,label="Pendentes: ")
		self.bAdd = wx.Button(self.pnl,label="&Adicionar")
		self.local = wx.Button(self.pnl,label="&Localizar")
		self.dateBox = wx.DatePickerCtrl(self.pnl)
		#self.dateC = wx.calendar.CalendarCtrl(self.pnl)
		self.taref = wx.TextCtrl(self.pnl)

		self.Size = (592,290)
		self.l1.Position = (0,0)
		self.l2.Position = (0,50)
		self.bAdd.Size = (171,27)
		self.bAdd.Position = (418,20)
		self.local.Size = (591,27)
		self.local.Position = (0,260)
		self.dateBox.Size = (110,27)
		self.dateBox.Position = (300,20)
		#self.dateC.Size = (291,179)
		#self.dateC.Position = (300,70)
		self.taref.Size = (91,181)
		self.taref.Position = (0,70)
		self.Center()

		self.Show(True)

def start():
	root = wx.App()
	MW(None)
	root.MainLoop()
