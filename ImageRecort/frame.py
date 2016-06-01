import wx
import ir

class Resize(wx.Frame):

	__slots__ = 'bOK','bCancel','ewidth','eheight','pnl','img','label'

	def __init__(self,*args,**kw):
		super(Resize,self).__init__(*args,**kw)
		self._pack()

	def _pack(self):
		self.pnl = wx.Panel(self)
		self.bOK = wx.Button(self.pnl,-1,"&Redimencionar")
		self.bCancel = wx.Button(self.pnl,-1,"&Cancelar")
		self.ewidth = wx.TextCtrl(self.pnl,-1,"")
		self.eheight = wx.TextCtrl(self.pnl,-1,"")
		self.lable = []
		self.label.append(wx.StaticText(self.pnl,-1,"Largura"))
		self.label.append(wx.StaticText(self.pnl,-1,"Altura"))
		self.img = None

		self.label[0].Position = (0,0)
		self.label[1].Position = (0,50)
		self.ewidth.Position = (0,20)
		self.eheight.Position = (0,70)
		self.ewidth.Size = (58,28)
		self.eheight.Size = (58,28)

		self.bOK.Position = (60,20)
		self.bCancel.Position = (60,48)

		self._events()

	def _events(self):
		self.bOK.Bind(wx.EVT_BUTTON,_resize)
		self.bCancel.Bind(wx.EVT_BUTTON,_cancel)

	def _cancel(self,evt):
		self.Close()

	def _resize(self,evt):
		w = int(ewidth.Value)
		h = int(eheight.Value)
		ir.resize(w,h,self.img)

	def _show(self,image):
		if image == "":
			return -1
		self.img = str(image)
		self.ShowModal()


class MainFrame(wx.Frame):

	__slots__ = 'pnl','eIn','eOut','ePosx','ePosy','eSizex','eSizey','eQual','bRec','resp','label','lPos','ePos','eSize','fdialog','bFind','resize','rr'

	def __init__(self,*args,**kwds):
		super(MainFrame,self).__init__(*args,**kwds)
		self._pack()

	def _pack(self):
		self.pnl = wx.Panel(self)
#		self.rr = Resize(None)
		self.eIn = wx.TextCtrl(self.pnl,-1,"")
		self.eOut = wx.TextCtrl(self.pnl,-1,"")
		self.ePosx = wx.TextCtrl(self.pnl,-1,"")
		self.ePosy = wx.TextCtrl(self.pnl,-1,"")
		self.eSizex = wx.TextCtrl(self.pnl,-1,"")
		self.eSizey = wx.TextCtrl(self.pnl,-1,"")
		self.eQual = wx.TextCtrl(self.pnl,-1,"")
		self.label = []
		self.bFind = []
		self.bFind.append(wx.Button(self.pnl,size=((28,28)),pos=((438,20)),label="..."))
		self.bFind.append(wx.Button(self.pnl,size=((28,28)),pos=((438,70)),label="..."))
#		self.resize = wx.Button(self.pnl,-1,"R&edimencionar")
		for i in range(0,7):
			self.label.append(wx.StaticText(self.pnl,-1,""))

		self.resp = wx.StaticText(self.pnl,-1,"")
		self.bRec = wx.Button(self.pnl,-1,"&Recortar")
		self.lPos = ((0,0),(0,50),(0,100),(60,100),(120,100),(180,100),(240,100))
		self.ePos = ((0,20),(0,70),(0,120),(60,120),(120,120),(180,120),(240,120))
		self.eSize = ((434,28),(434,28),(58,28),(58,28),(58,27),(58,28),(58,28))

		self.Size = (466,148)
		self.SetTitle("Recorta Imagem")

		ltext = ('Arquivo de entrada','Arquivo de saida','Pos x','Pos y','Largura','Altura','Qualidade')
		for i in range(0,7):
			self.label[i].Position = self.lPos[i]
			self.label[i].Label = ltext[i]
		self.eIn.Position = self.ePos[0]
		self.eOut.Position = self.ePos[1]
		self.ePosx.Position = self.ePos[2]
		self.ePosy.Position = self.ePos[3]
		self.eSizex.Position = self.ePos[4]
		self.eSizey.Position = self.ePos[5]
		self.eQual.Position = self.ePos[6]

		self.eIn.Size = self.eSize[0]
		self.eOut.Size = self.eSize[1]
		self.ePosx.Size = self.eSize[2]
		self.ePosy.Size = self.eSize[3]
		self.eSizex.Size = self.eSize[4]
		self.eSizey.Size = self.eSize[5]
		self.eQual.Size = self.eSize[6]

		self.bRec.Size = (80,28)
#		self.resize.Size = (84,28)
		self.bRec.Position = (300,120)
#		self.resize.Position = (382,120)

		self._events()

	def _events(self):
		self.bRec.Bind(wx.EVT_BUTTON,self._recortar)
		self.bFind[0].Bind(wx.EVT_BUTTON,self._openFile)
		self.bFind[1].Bind(wx.EVT_BUTTON,self._saveFile)

	def _recortar(self,evt):
		_in = str(self.eIn.Value)
		_out = str(self.eOut.Value)
		_resol = int(self.eQual.Value)
		_x = int(self.ePosx.Value)
		_y = int(self.ePosy.Value)
		_w = int(self.eSizex.Value)
		_h = int(self.eSizey.Value)

		print _in,_out,_resol,_x,_y,_w,_h

		#try:
		ir.recImage(_in,_out,_resol,_x,_y,_w,_h)
		#except:
		#	print "Erro ao iniciar a function."

	def _openFile(self,evt):
		self.fdialog = wx.FileDialog(self,style=wx.OPEN,message="Abrir...")
		self.fdialog.ShowModal()
		self.eIn.Value = self.fdialog.Path

	def _saveFile(self,evt):
		self.fdialog = wx.FileDialog(self,style=wx.SAVE,message="Salvar...")
		self.fdialog.ShowModal()
		self.eOut.Value = self.fdialog.Path

	def _resize(self,evt):
		#self.rr._show(self.eIn.Value)
		print ""


app = wx.App()
win = MainFrame(None)
win.Show()
app.MainLoop() 
