#!/usr/bin/python 
# buttons.py
import time
import wx
import random
import Consulta_nombres_gerentes
import Insert_mySQL
import Consulta_busqueda
import UPDATE


consulta = Consulta_nombres_gerentes.consultas('Registro','Recursos_H')
consulta = consulta.consultar()


class MyButtons(wx.Dialog):
	def __init__(self, parent, id, title): 
		wx.Dialog.__init__(self, parent, id, title, size=(544, 297))
		# ---- // ---- 
		#self.statusBar1 = wx.StatusBar(self,id=3,name='statusBar1',style=0)
		# ---- // ---- 
		wx.StaticText(self,id=5, pos=(16, 16), size=(76, 17),name='staticText1',label='id')
		wx.StaticText(self,id=6, pos=(16, 48), size=(76, 17),name='staticText2',label='nombre')
		wx.StaticText(self,id=7, pos=(16, 80), size=(83, 17),name='staticText3',label='responsable')
		wx.StaticText(self,id=8, pos=(16, 112), size=(76, 17),name='staticText4',label='fecha')
		wx.StaticText(self,id=9, pos=(230, 16), size=(76, 17),name='staticText5',label='estado')
		wx.StaticText(self,id=10, pos=(230, 48), size=(76, 17),name='staticText6',label='Tipo')
		# ---- // ---- 
		#TextContrl1 = wx.TextCtrl(self,id=10, name='textCtrl1', pos=(110, 15), size=(80, 25), value='')
		global TextContrl2 
		global TextContrlid
		TextContrl2= wx.TextCtrl(self,id=11, name='textCtrl2', pos=(110, 47), size=(80, 27), value='')
		TextContrlid = wx.TextCtrl(self,id=12, name='textCtrl3', pos=(110, 15), size=(80, 27), value='')
		#--------------------------------------------------------------------------------------------
		localtime = time.asctime( time.localtime(time.time()))		# FECHA Y HORA
		global TextTime
		TextTime = wx.StaticText(self,id=13, pos=(110, 111), size=(180, 27),name='staticText7',label=localtime)
		#--------------------------------------------------------------------------------------------
		global ComboBox1
		global ComboBox2
		global ComboBox3
		ComboBox1 = self.curso=wx.ComboBox(self,14,'evaluando',pos=(298, 15),size=(110, 27),choices=['evaluando','aceptado','iniciado','cerrado','cancelado'])
		ComboBox2 = self.curso=wx.ComboBox(self,15,'interno',pos=(298, 47),size=(110, 27),choices=['interno','externo'])
		ComboBox3 = self.curso=wx.ComboBox(self,16,'',pos=(110, 79),size=(110, 27),choices= consulta)
		
		# ---- // ---- 
		wx.Button(self, 1, 'Close', (20, 150), (85, 29))
		wx.Button(self, 2, 'Dar de alta', (120, 150), (85, 29))
		wx.Button(self, 3, 'actualizar', (220, 150), (85, 29))
		wx.Button(self, 4, 'Buscar', (320, 150), (85, 29))
		
		# ---- /para Busqueda/ ----
		mylistbox=[]
		# ---- // ----
			
		self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)
		self.Bind(wx.EVT_BUTTON, self.OnRandomMove, id=2)
		self.Bind(wx.EVT_BUTTON, self.OnActualizar, id=3)
		self.Bind(wx.EVT_BUTTON, self.OnBusqueda, id=4)
	#	
		self.Centre()
		self.ShowModal()
		self.Destroy()
 
	def OnClose(self, event):
		self.Close(True)
		self.Destroy()
 
	def OnRandomMove(self, event):
		#GetId=TextContrlid.GetValue()	==>  se pone automatico
		GetNombre=TextContrl2.GetValue()
		GetResponsable = ComboBox3.GetValue()
		#GetTime = TextTime.GetValue()  ==>  se pone automatico
		GetEstado = ComboBox1.GetValue()
		GetType = ComboBox2.GetValue()
		insertar1 = Insert_mySQL.Insertar('Registro','Proyects',GetNombre,GetResponsable,GetEstado,GetType)
		insertar1.syntaxis_insert()
	
	def OnBusqueda(self, event):
		global GetId
		global GetNombre
		global GetResponsable
		global GetEstado
		global GetType
		GetId=TextContrlid.GetValue()	
		GetNombre=TextContrl2.GetValue()
		GetResponsable = ComboBox3.GetValue()
		#GetTime = TextTime.GetValue() 
		GetEstado = ComboBox1.GetValue()
		GetType = ComboBox2.GetValue()
				
		Busqueda1 = Consulta_busqueda.Busquedas('Registro','Proyects',GetId,GetNombre,GetResponsable,'',GetEstado,GetType)
		Busqueda1 = Busqueda1.Busqueda()
		
		global ListBox
		ListBox = wx.ListBox(self, id=17, pos=(20,190), size=(500,60), choices=Busqueda1, style=wx.LB_SINGLE)
	
		
	def OnActualizar(self, event):	
		GetNombre=TextContrl2.GetValue()
		GetResponsable = ComboBox3.GetValue()
		#GetTime = TextTime.GetValue() 
		GetEstado = ComboBox1.GetValue()
		GetType = ComboBox2.GetValue()
		
		selectionList=str(ListBox.GetSelection()+1) 	# ME QUEDE ACA QUIERO OBTENER LA POSICION LA CONSULTA QUE ESTOY SELECCIONANDO EN LA LIST BOX
		#selectionList=ListBox.GetString()
		#SelectionList = ListBox[0]
		print selectionList
		Modificacion1 = UPDATE.MOD('Registro','Proyects',selectionList,GetNombre,GetResponsable,GetEstado,GetType)
		Modificacion1 = Modificacion1.syntaxis_MOD()
		
		

app = wx.App(0)
MyButtons(None, -1, 'buttons.py')
app.MainLoop()

