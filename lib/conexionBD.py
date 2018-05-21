import sqlite3

class ConexionBD: 
	def __init__(self):
		
		self.con = sqlite3.connect("db/agenda.ab")
		self.c = self.con.cursor()
		#print "funciona"

	def crear_tabla(self):
		
		self.c.execute("create table if not exists t_agenda ('nombre' varchar, 'apellido' varchar, 'telefono' varchar, 'email' varchar, 'fecha_nacimiento' varchar)")
		
		

	def insertar(self, name, ape, tel, e_mail, y,m,d):
		
		self.nombre = name
		self.apellido = ape
		self.telefono = tel
		self.email = e_mail
		#self.fecha_nacimiento = fecha_nac
		self.anio=y
		self.mes=m
		self.dia=d
	
		self.c.execute("insert into t_agenda values('"+ self.nombre + "','" + self.apellido + "','" + self.telefono +"','" + self.email + "','"+self.dia+"/"+self.mes+"/"+self.anio+"')")
		self.con.commit()
	
		#print "se insertaron datos"

	def select_all(self):
		
		sql=self.c.execute("select * from t_agenda")
		self.imprimir_sql(sql)

	def actualizar_datos(self,columna,nuevo_dato,email):
		sql=self.c.execute("update t_agenda set " + columna + "='" + nuevo_dato + "' where email='" + email + "'")
		self.con.commit()

	def buscar(self,dato,dato2):
		sql=self.c.execute("select * from t_agenda where apellido LIKE '%" + dato + "' and email='" + dato2+ "'")
		self.imprimir_sql(sql)
			
	def eliminar_datos(self,dato):
		self.c.execute("delete from t_agenda where email='" + dato + "'")
		self.con.commit()

	def imprimir_sql(self, sql):
		registros = self.c.fetchall()
		print "Nombre | Apellido | Telefono | Email | Fecha de Nacimiento "
		print "------------------------------------------------------------"
		for registro in registros: 
			name= registro[0]
			ape= registro[1]
			tel=registro[2]
			email = registro[3]
			fecha_nac = registro[4]
			print name + "  | "  + ape + "  | " + tel + "  | " + email + "  | " + fecha_nac

	def cantidad_registros(self):
		self.c.execute("select count(*) from t_agenda")
		registros=self.c.fetchone()
		return registros

	
	def desconectar_bd(self):
		self.con.close()