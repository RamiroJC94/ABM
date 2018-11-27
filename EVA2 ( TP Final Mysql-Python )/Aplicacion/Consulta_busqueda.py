# modificacion de consulta_espesifica

import MySQLdb as mdb

class Busquedas:
	def __init__ (self, dbName, Table, ID_proy, nombre, respon,fecha, estado, Tipo):
		self.databaseName = dbName
		self.TableName = Table
		self.ID_P = ID_proy
		self.nom = nombre
		self.res= respon
		self.est = estado
		self.Type = Tipo
		self.fech = fecha
		
	def Busqueda (self):
		con = mdb.connect('localhost', 'usuario', '42167895', self.databaseName)
		with con:
			cur = con.cursor(mdb.cursors.DictCursor)
			#cur.execute("SELECT nombre FROM `"+self.databaseName+"`.`"+self.TableName+"` WHERE posicion='gerente'")
			cur.execute("SELECT ID_Proyect, nombre, responsable, fecha_init, estado, Type_proyect FROM Proyects WHERE ID_Proyect LIKE '%"+self.ID_P+"%' AND nombre LIKE '%"+self.nom+"%' AND responsable LIKE '%"+self.res+"%' AND fecha_init LIKE '%"+self.fech+"%' AND estado LIKE '%"+self.est+"%' AND Type_proyect LIKE '%"+self.Type+"%';")
			rows = cur.fetchall()
			Lista=[]
			for row in rows:
				#print row["ID_Proyect"], row["nombre"] , row["fecha_init"],row["responsable"], row["estado"]
				#esta comentado por que para este caso no se necesita pero ya que esta ... ... ...  
				fecha = str(row["fecha_init"])
				print fecha
				#Lista.append("str(row["ID_Proyect"]), str(row["nombre"]),str(fecha) ,str(row["responsable"]), str(row["estado"]))
				Lista.append( ""+str(row["ID_Proyect"])+" "+str(row["nombre"])+" "+str(fecha)+" "+str(row["responsable"])+" "+str(row["estado"]) )
				
			print Lista
			print 'cantidad de Proyects',len(Lista)
			return Lista
