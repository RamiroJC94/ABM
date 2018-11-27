# modificacion de consulta_espesifica

import MySQLdb as mdb

class consultas:
	def __init__ (self, dbName, Table, nombre, respon, estado, Tipo):
		self.databaseName = dbName
		self.TableName = Table
		self.nom = nombre
		self.res= respon
		self.est = estado
		self.Type = Tipo
		
	def consultar (self):
		con = mdb.connect('localhost', 'usuario', '42167895', self.databaseName)
		with con:
			cur = con.cursor(mdb.cursors.DictCursor)
			#cur.execute("UPDATE "+self.ColumName+" FROM "+self.TableName)
			cur.execute("UPDATE `Registro`.`Proyects` SET nombre='"+self.nom+"', responsable='"+self.res+"',estado='"+self.est+"',Type_proyect='"+self.Type+"' where # aca tiene que ir el resultado de la busqueda")
			
