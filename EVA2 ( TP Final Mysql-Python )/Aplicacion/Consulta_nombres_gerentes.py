# modificacion de consulta_espesifica

import MySQLdb as mdb

class consultas:
	def __init__ (self, dbName, Table):
		self.databaseName = dbName
		self.TableName = Table
		
	def consultar (self):
		con = mdb.connect('localhost', 'usuario', '42167895', self.databaseName)
		with con:
			cur = con.cursor(mdb.cursors.DictCursor)
			#cur.execute("SELECT nombre FROM `"+self.databaseName+"`.`"+self.TableName+"` WHERE posicion='gerente'")
			cur.execute("SELECT Legajo, nombre FROM Recursos_H WHERE posicion='gerente'")
			rows = cur.fetchall()
			Lista=[]
			for row in rows:
				print row["Legajo"], row["nombre"] #, row["fecha_init"],row["responsable"], row["estado"]
				#esta comentado por que para este caso no se necesita pero ya que esta ... ... ...  
				Lista.insert(row["Legajo"],row["nombre"])
			print Lista
			print 'cantidad de Proyects',len(Lista)
			return Lista
 
