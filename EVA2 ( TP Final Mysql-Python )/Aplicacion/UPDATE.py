# modificacion de consulta_espesifica

import MySQLdb as mdb

class MOD:
	def __init__ (self, dbName, Table, ID_proy, nombre, respon, estado, Tipo):
		self.databaseName = dbName
		self.TableName = Table
		self.ID_P = ID_proy
		self.nom = nombre
		self.res= respon
		self.est = estado
		self.Type = Tipo
		
	def syntaxis_MOD (self):
		con = mdb.connect('localhost', 'usuario', '42167895', self.databaseName)
		with con:
			cur = con.cursor(mdb.cursors.DictCursor)
			#cur.execute("INSERT INTO `"+self.databaseName+"`.`"+self.TableName+"`(`ID_Proyect`,`nombre`,`responsable`,`fecha_init`,`estado`,`Type_Proyect`) VALUES (NULL,"+self.nom+","+self.res+",CURRENT_TIMESTAMP,"+self.est+","+self.Type) 
			#cur.execute("INSERT INTO `"+self.databaseName+"`.`"+self.TableName+"`(`ID_Proyect`,`nombre`,`responsable`,`fecha_init`,`estado`,`Type_Proyect`) VALUES (NULL,'"+self.nom+"','"+self.res+"',CURRENT_TIMESTAMP,'"+self.est+"','"+self.Type+"')")             
			cur.execute("UPDATE `"+self.databaseName+"`.`"+self.TableName+"` SET `nombre` = '"+self.nom+"', `responsable` = '"+self.res+"',`estado`='"+self.est+"' where `ID_Proyect`='"+self.ID_P+"'")
			print ('echo')
			
			
